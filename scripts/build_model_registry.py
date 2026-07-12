"""Write results/model-registry.csv from the canonical Python registry."""

from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from llm_econ_beliefs.model_registry import write_model_registry_csv  # noqa: E402


def main() -> int:
    primary = write_model_registry_csv()
    print(f"Wrote {primary}")

    # dashboard/results is the build-root fallback used when Vercel cannot read
    # the repository-level results directory. It is a generated staging copy,
    # not a second metadata source.
    dashboard_copy = REPO_ROOT / "dashboard" / "results" / "model-registry.csv"
    write_model_registry_csv(dashboard_copy)
    print(f"Staged {dashboard_copy}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
