"""Registry-driven complete-grid gating for analysis artifact builders."""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence, TextIO

try:
    from check_panel_grid import check_batch_directory
except ModuleNotFoundError:  # Imported as ``scripts.panel_grid_gate`` in tests.
    from scripts.check_panel_grid import check_batch_directory


@dataclass(frozen=True)
class PanelGridGate:
    included_models: tuple[str, ...]
    excluded_models: tuple[str, ...]
    incomplete_models: tuple[str, ...]
    errors_by_model: dict[str, tuple[str, ...]]


def gate_panel_models(
    results_root: Path,
    model_ids: Sequence[str],
    *,
    allow_partial: bool = False,
    stream: TextIO = sys.stdout,
) -> PanelGridGate:
    """Check every declared main-panel grid and exclude incomplete models."""
    complete: list[str] = []
    incomplete: list[str] = []
    errors_by_model: dict[str, tuple[str, ...]] = {}
    for model_id in model_ids:
        result = check_batch_directory(
            results_root,
            model_name=model_id,
            batch="elasticities-batch15",
            require_parsed=True,
        )
        if result.ok:
            complete.append(model_id)
        else:
            incomplete.append(model_id)
            errors_by_model[model_id] = result.errors

    included = list(model_ids) if allow_partial else complete
    excluded = [] if allow_partial else incomplete
    payload = {
        "event": "panel_grid_exclusions",
        "batch": "elasticities-batch15",
        "allow_partial": allow_partial,
        "declared_models": list(model_ids),
        "incomplete_models": incomplete,
        "excluded_models": excluded,
        "errors_by_model": {
            model_id: list(errors_by_model[model_id]) for model_id in incomplete
        },
    }
    print(
        "PANEL_GRID_EXCLUSIONS=" + json.dumps(payload, sort_keys=True),
        file=stream,
    )
    return PanelGridGate(
        included_models=tuple(included),
        excluded_models=tuple(excluded),
        incomplete_models=tuple(incomplete),
        errors_by_model=errors_by_model,
    )
