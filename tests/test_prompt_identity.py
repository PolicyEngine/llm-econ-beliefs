"""CI gate for the paper's prompt-wording disclosure.

The archived request logs, the manuscript, and the audit table are all
committed, so this check is hermetic in CI: it recomputes the per-quantity
prompt census from ``results/*-elasticities-batch15/runs.jsonl`` and fails
if the paper's disclosure (23 of 26 quantities byte-identical across all 28
models; the three sign-clarified quantities split 21/7 on the same seven
April models) drifts from the archives, or the archives from the current
prompt builder. The rest of ``verify_paper_prose.py`` stays a local build
gate; this census is the piece where silent drift would misstate the
elicitation protocol itself.
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import verify_paper_prose  # noqa: E402


def test_prompt_identity_census_matches_paper_disclosure():
    verify_paper_prose.FAILURES.clear()
    verify_paper_prose.verify_prompt_identity()
    assert not verify_paper_prose.FAILURES, verify_paper_prose.FAILURES
