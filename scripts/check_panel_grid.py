"""Validate canonical panel result files against their exact expected grids.

The checker is intentionally read-only.  It treats missing, unexpected, and
duplicate ``(model, prompt_version, quantity, run_index)`` keys as failures.
Use ``--require-parsed`` when completeness also requires every expected slot
to contain a successfully parsed response.

``validate_cell_identity`` extends the grid with what was actually sent: the
provider tag, tool regime and prompt text of every row.  The runners use it
before reusing stored answers, so a cell elicited under a different prompt,
provider or tool regime is re-elicited instead of republished.

Usage:
    .venv/bin/python scripts/check_panel_grid.py \
        --models deepseek-v4-pro,qwen-3.7-max --require-parsed
"""

from __future__ import annotations

import argparse
import dataclasses
import json
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Collection, Iterable, Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from llm_econ_beliefs import list_quantities
from llm_econ_beliefs.model_registry import MODEL_REGISTRY, PANEL_MODEL_IDS
from llm_econ_beliefs.provider_tags import (
    LITELLM_COMPLETION_PROVIDER,
    OPENAI_CHAT_COMPLETIONS_PROVIDER,
    provider_tag_for_runner,
)
from llm_econ_beliefs.runner import build_run_grid


RUNS_PER_QUANTITY = 15
# The no-argument invocation verifies exactly the completeness the paper
# claims: the main elasticities batch for every registry model, plus the
# clarify batches for every wave after April 2026. Three April models
# carry documented clarify-batch gaps (claude-opus-4.7's armington runs
# are tagged v4; two Gemini previews hold unparsed clarify slots), so
# April clarify cells are only checked when named explicitly via --models.
POST_APRIL_MODEL_IDS = tuple(
    model.model_id for model in MODEL_REGISTRY if model.wave != "april_2026"
)
BATCH_PROMPT_VERSIONS = {
    "elasticities-batch15": "v4",
    "armington-clarify-batch15": "armington-clarify",
    "ies-clarify-batch15": "ies-clarify",
}

# Early revisions of scripts/rerun_failed_runs.py tagged replacement rows with
# the bare runner key. The committed gpt-5.5, grok-4.3 and qwen-3.7-max
# archives still hold such rows; each key names the same serving path as its
# canonical tag.
LEGACY_PROVIDER_TAGS = {
    "openai": OPENAI_CHAT_COMPLETIONS_PROVIDER,
    "litellm": LITELLM_COMPLETION_PROVIDER,
}

# The seven April models elicited before the April 21 clarifier revision keep
# the original wording on the three sign-clarified quantities (disclosed in the
# manuscript's Design section and pinned by scripts/verify_paper_prose.py).
# This is the only stored prompt text allowed to differ from today's builder.
SIGN_CLARIFIED_QUANTITIES = (
    "labor_supply.income_elasticity.prime_age",
    "tax.capital_gains_realizations.elasticity",
    "tax.capital_gains_realizations.elasticity.net_of_tax_rate",
)
ORIGINAL_WORDING_MODELS = frozenset(
    {
        "claude-haiku-4.5",
        "gemini-3-flash-preview",
        "gemini-3.1-flash-lite-preview",
        "gpt-5.4",
        "gpt-5.4-mini",
        "gpt-5.4-nano",
        "grok-4.1-fast",
    }
)

GridKey = tuple[str, str, str, int]


@dataclass(frozen=True)
class GridCheckResult:
    """Result of checking one set of run records."""

    expected_count: int
    observed_count: int
    errors: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return not self.errors


@dataclass(frozen=True)
class CellIdentity:
    """Everything stored runs must share to stand for one model/batch cell.

    ``provider`` is a canonical artifact tag and ``prompts`` maps each
    quantity id to the exact prompt text the elicitation sends.
    """

    model_name: str
    provider: str
    prompt_version: str
    tool_regime: str
    prompts: Mapping[str, str]
    n_runs: int = RUNS_PER_QUANTITY

    def __post_init__(self) -> None:
        if not self.prompts:
            raise ValueError("a cell identity needs at least one quantity")
        object.__setattr__(self, "prompts", MappingProxyType(dict(self.prompts)))

    @property
    def quantity_ids(self) -> tuple[str, ...]:
        return tuple(self.prompts)

    def restricted_to(self, quantity_ids: Sequence[str]) -> CellIdentity:
        """Return the identity of a sub-cell holding only ``quantity_ids``."""
        unknown = [
            quantity_id for quantity_id in quantity_ids if quantity_id not in self.prompts
        ]
        if unknown:
            raise KeyError(f"quantities outside this cell: {unknown}")
        return dataclasses.replace(
            self,
            prompts={
                quantity_id: self.prompts[quantity_id] for quantity_id in quantity_ids
            },
        )


def quantity_ids_for_batch(batch: str) -> list[str]:
    """Return the quantities expected in one canonical batch."""
    if batch == "elasticities-batch15":
        return [quantity.id for quantity in list_quantities()]
    if batch == "armington-clarify-batch15":
        return ["trade.armington_elasticity.import_domestic"]
    if batch == "ies-clarify-batch15":
        return ["household.intertemporal_elasticity_of_substitution"]
    raise ValueError(f"Unknown batch: {batch}")


def expected_grid_keys(
    *,
    model_name: str,
    prompt_version: str,
    quantity_ids: Sequence[str],
    n_runs: int = RUNS_PER_QUANTITY,
) -> set[GridKey]:
    """Build the exact expected key set for one model/batch cell."""
    if not model_name:
        raise ValueError("model_name must not be empty")
    if not prompt_version:
        raise ValueError("prompt_version must not be empty")
    if not quantity_ids:
        raise ValueError("quantity_ids must not be empty")
    if n_runs <= 0:
        raise ValueError("n_runs must be positive")
    return {
        (model_name, prompt_version, quantity_id, run_index)
        for quantity_id in quantity_ids
        for run_index in range(1, n_runs + 1)
    }


def validate_grid_rows(
    rows: Iterable[Mapping[str, object]],
    *,
    model_name: str,
    prompt_version: str,
    quantity_ids: Sequence[str],
    n_runs: int = RUNS_PER_QUANTITY,
    require_parsed: bool = False,
) -> GridCheckResult:
    """Check already-decoded run rows against an exact expected grid."""
    expected = expected_grid_keys(
        model_name=model_name,
        prompt_version=prompt_version,
        quantity_ids=quantity_ids,
        n_runs=n_runs,
    )
    counts: Counter[GridKey] = Counter()
    parsed_by_key: dict[GridKey, list[object]] = {}
    malformed: list[str] = []
    observed_count = 0

    for row_number, row in enumerate(rows, 1):
        observed_count += 1
        try:
            key = (
                row["model_name"],
                row["prompt_version"],
                row["quantity_id"],
                row["run_index"],
            )
        except KeyError as exc:
            malformed.append(f"row {row_number} missing field {exc.args[0]!r}")
            continue
        if (
            not isinstance(key[0], str)
            or not isinstance(key[1], str)
            or not isinstance(key[2], str)
            or not isinstance(key[3], int)
            or isinstance(key[3], bool)
        ):
            malformed.append(f"row {row_number} has invalid grid-key types: {key!r}")
            continue
        typed_key: GridKey = key
        counts[typed_key] += 1
        parsed_by_key.setdefault(typed_key, []).append(row.get("parsed_ok"))

    actual = set(counts)
    missing = sorted(expected - actual)
    unexpected = sorted(actual - expected)
    duplicates = sorted((key, count) for key, count in counts.items() if count != 1)
    unparsed = sorted(
        key
        for key in expected & actual
        if require_parsed
        and not (len(parsed_by_key.get(key, ())) == 1 and parsed_by_key[key][0] is True)
    )

    errors = list(malformed)
    if missing:
        errors.append(_format_key_problem("missing", missing))
    if unexpected:
        errors.append(_format_key_problem("unexpected", unexpected))
    if duplicates:
        errors.append(_format_key_problem("duplicate", duplicates))
    if unparsed:
        errors.append(_format_key_problem("unparsed", unparsed))
    return GridCheckResult(
        expected_count=len(expected),
        observed_count=observed_count,
        errors=tuple(errors),
    )


def _format_key_problem(label: str, values: Sequence[object]) -> str:
    preview = ", ".join(repr(value) for value in values[:5])
    suffix = "" if len(values) <= 5 else f", ... ({len(values)} total)"
    return f"{label}: {preview}{suffix}"


def expected_cell_identity(
    *,
    model_name: str,
    runner: str,
    prompt_version: str,
    quantity_ids: Sequence[str],
    tool_regime: str = "none",
    n_runs: int = RUNS_PER_QUANTITY,
) -> CellIdentity:
    """Build the identity a fresh elicitation of this cell would carry.

    Prompts come from the same ``build_run_grid`` call the ``--exec-cell``
    child makes, and ``runner`` is the provider key that child is given.
    """
    grid = build_run_grid(
        model_names=[model_name],
        quantity_ids=quantity_ids,
        n_runs=1,
        prompt_version=prompt_version,
        tool_regime=tool_regime,
    )
    return CellIdentity(
        model_name=model_name,
        provider=provider_tag_for_runner(runner),
        prompt_version=prompt_version,
        tool_regime=tool_regime,
        prompts={run.quantity_id: run.prompt for run in grid},
        n_runs=n_runs,
    )


def _as_row(row: object) -> Mapping[str, object]:
    if dataclasses.is_dataclass(row) and not isinstance(row, type):
        return dataclasses.asdict(row)
    return row  # type: ignore[return-value]


def validate_cell_identity(
    rows: Iterable[object],
    identity: CellIdentity,
    *,
    require_parsed: bool,
    exact_prompts: bool = True,
    allowed_drift: Collection[str] = (),
    accept_legacy_provider_tags: bool = False,
) -> GridCheckResult:
    """Check that rows are exactly the cell ``identity`` describes.

    On top of the exact grid this rejects any row whose provider tag, tool
    regime or prompt differs from the identity, and any quantity whose rows
    carry more than one prompt text.  ``allowed_drift`` names quantities whose
    stored prompt may differ from today's builder (an older, disclosed
    wording); ``exact_prompts=False`` waives that comparison for every
    quantity.  Either way a cell must be internally uniform.  Rows may be
    mappings or ``RunResult``-like dataclasses.
    """
    rows = [_as_row(row) for row in rows]
    grid = validate_grid_rows(
        rows,
        model_name=identity.model_name,
        prompt_version=identity.prompt_version,
        quantity_ids=identity.quantity_ids,
        n_runs=identity.n_runs,
        require_parsed=require_parsed,
    )

    wrong_provider: list[object] = []
    wrong_tool_regime: list[object] = []
    non_text_prompt: list[object] = []
    wrong_prompt: list[object] = []
    texts_by_quantity: dict[str, set[str]] = {}
    for row in rows:
        quantity_id = row.get("quantity_id")
        slot = (quantity_id, row.get("run_index"))
        provider = row.get("provider")
        if accept_legacy_provider_tags and isinstance(provider, str):
            provider = LEGACY_PROVIDER_TAGS.get(provider, provider)
        if provider != identity.provider:
            wrong_provider.append(slot)
        if row.get("tool_regime") != identity.tool_regime:
            wrong_tool_regime.append(slot)
        prompt = row.get("prompt")
        if not isinstance(prompt, str) or not prompt.strip():
            non_text_prompt.append(slot)
            continue
        if not isinstance(quantity_id, str):
            continue  # already reported as a malformed grid key
        texts_by_quantity.setdefault(quantity_id, set()).add(prompt)
        if (
            exact_prompts
            and quantity_id not in allowed_drift
            and quantity_id in identity.prompts
            and prompt != identity.prompts[quantity_id]
        ):
            wrong_prompt.append(slot)

    mixed = sorted(
        quantity_id for quantity_id, texts in texts_by_quantity.items() if len(texts) > 1
    )
    errors = list(grid.errors)
    if wrong_provider:
        errors.append(
            _format_key_problem(f"provider is not {identity.provider!r}", wrong_provider)
        )
    if wrong_tool_regime:
        errors.append(
            _format_key_problem(
                f"tool_regime is not {identity.tool_regime!r}", wrong_tool_regime
            )
        )
    if non_text_prompt:
        errors.append(_format_key_problem("prompt is missing or empty", non_text_prompt))
    if wrong_prompt:
        errors.append(
            _format_key_problem("prompt differs from the current builder", wrong_prompt)
        )
    if mixed:
        errors.append(_format_key_problem("more than one prompt text", mixed))
    return GridCheckResult(
        expected_count=grid.expected_count,
        observed_count=grid.observed_count,
        errors=tuple(errors),
    )


def documented_prompt_drift(model_name: str, prompt_version: str) -> frozenset[str]:
    """Quantities whose archived prompt may predate today's builder text."""
    if prompt_version == "v4" and model_name in ORIGINAL_WORDING_MODELS:
        return frozenset(SIGN_CLARIFIED_QUANTITIES)
    return frozenset()


def drifted_prompt_quantities(
    rows: Iterable[object], identity: CellIdentity
) -> list[str]:
    """Quantities whose stored prompt text differs from today's builder."""
    drifted: set[str] = set()
    for row in map(_as_row, rows):
        quantity_id = row.get("quantity_id")
        if (
            isinstance(quantity_id, str)
            and quantity_id in identity.prompts
            and row.get("prompt") != identity.prompts[quantity_id]
        ):
            drifted.add(quantity_id)
    return sorted(drifted)


def check_canonical_cell(
    directory: Path,
    identity: CellIdentity,
    *,
    require_parsed: bool,
) -> tuple[GridCheckResult, list[str]]:
    """Check a committed ``results/<model>-<batch>`` directory's identity.

    Stored prompts must equal today's builder text except where
    ``documented_prompt_drift`` allows the seven April models' original
    clarifier wording, and legacy provider tags are normalized.  Returns the
    result and the quantities whose stored prompt differs from today's builder.
    """
    rows, read_errors = load_jsonl_rows([directory / "runs.jsonl"])
    result = validate_cell_identity(
        rows,
        identity,
        require_parsed=require_parsed,
        allowed_drift=documented_prompt_drift(
            identity.model_name, identity.prompt_version
        ),
        accept_legacy_provider_tags=True,
    )
    return (
        GridCheckResult(
            expected_count=result.expected_count,
            observed_count=result.observed_count,
            errors=tuple(read_errors) + result.errors,
        ),
        drifted_prompt_quantities(rows, identity),
    )


def load_jsonl_rows(paths: Iterable[Path]) -> tuple[list[dict[str, object]], list[str]]:
    """Read JSONL rows without modifying any input file."""
    rows: list[dict[str, object]] = []
    errors: list[str] = []
    for path in paths:
        if not path.exists():
            errors.append(f"missing file: {path}")
            continue
        try:
            # Split on "\n" only, as iterating the file would; splitlines()
            # would also break inside strings holding U+2028 and similar.
            lines = path.read_text(encoding="utf-8").split("\n")
        except (OSError, UnicodeDecodeError) as exc:
            errors.append(f"unreadable file: {path}: {exc}")
            continue
        for line_number, line in enumerate(lines, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"{path}:{line_number}: invalid JSON: {exc.msg}")
                continue
            if not isinstance(row, dict):
                errors.append(f"{path}:{line_number}: expected a JSON object")
                continue
            rows.append(row)
    return rows, errors


def check_run_files(
    paths: Iterable[Path],
    *,
    model_name: str,
    prompt_version: str,
    quantity_ids: Sequence[str],
    n_runs: int = RUNS_PER_QUANTITY,
    require_parsed: bool = False,
) -> GridCheckResult:
    """Read one or more run files and check their combined exact grid."""
    rows, read_errors = load_jsonl_rows(paths)
    result = validate_grid_rows(
        rows,
        model_name=model_name,
        prompt_version=prompt_version,
        quantity_ids=quantity_ids,
        n_runs=n_runs,
        require_parsed=require_parsed,
    )
    return GridCheckResult(
        expected_count=result.expected_count,
        observed_count=result.observed_count,
        errors=tuple(read_errors) + result.errors,
    )


def check_batch_directory(
    results_root: Path,
    *,
    model_name: str,
    batch: str,
    require_parsed: bool = False,
) -> GridCheckResult:
    """Check one canonical ``results/<model>-<batch>`` directory."""
    return check_run_files(
        [results_root / f"{model_name}-{batch}" / "runs.jsonl"],
        model_name=model_name,
        prompt_version=BATCH_PROMPT_VERSIONS[batch],
        quantity_ids=quantity_ids_for_batch(batch),
        require_parsed=require_parsed,
    )


def _parse_csv_list(raw: str, *, option: str) -> list[str]:
    values = [value.strip() for value in raw.split(",") if value.strip()]
    if not values:
        raise ValueError(f"{option} must contain at least one value")
    if len(values) != len(set(values)):
        raise ValueError(f"{option} must not contain duplicates")
    return values


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--models",
        default=None,
        help=(
            "comma-separated model names (default: the full registry for the "
            "main batch, July-wave models for the clarify batches)"
        ),
    )
    parser.add_argument(
        "--batches",
        default=None,
        help="comma-separated canonical batch suffixes",
    )
    parser.add_argument(
        "--results-root",
        type=Path,
        default=REPO_ROOT / "results",
    )
    parser.add_argument(
        "--require-parsed",
        action="store_true",
        help="also require parsed_ok=true for every expected slot",
    )
    args = parser.parse_args()

    try:
        models = (
            _parse_csv_list(args.models, option="--models")
            if args.models is not None
            else None
        )
        batches = (
            _parse_csv_list(args.batches, option="--batches")
            if args.batches is not None
            else None
        )
    except ValueError as exc:
        parser.error(str(exc))
    if batches is not None:
        unknown_batches = sorted(set(batches) - set(BATCH_PROMPT_VERSIONS))
        if unknown_batches:
            parser.error(f"unknown batches: {', '.join(unknown_batches)}")

    if models is None and batches is None:
        # The paper-claim plan: main batch panel-wide, clarify July-wide.
        plan = [(model, "elasticities-batch15") for model in PANEL_MODEL_IDS]
        plan += [
            (model, batch)
            for model in POST_APRIL_MODEL_IDS
            for batch in ("armington-clarify-batch15", "ies-clarify-batch15")
        ]
    else:
        plan = [
            (model, batch)
            for model in (models if models is not None else PANEL_MODEL_IDS)
            for batch in (batches if batches is not None else BATCH_PROMPT_VERSIONS)
        ]

    all_ok = True
    for model_name, batch in plan:
        result = check_batch_directory(
            args.results_root,
            model_name=model_name,
            batch=batch,
            require_parsed=args.require_parsed,
        )
        label = f"{model_name}/{batch}"
        if result.ok:
            print(f"OK {label}: {result.observed_count}/{result.expected_count}")
            continue
        all_ok = False
        print(
            f"FAIL {label}: {result.observed_count}/{result.expected_count}",
            file=sys.stderr,
        )
        for error in result.errors:
            print(f"  {error}", file=sys.stderr)
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
