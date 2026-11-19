"""The /paper wrapper and its embedded render stay in lockstep.

The wrapper page pins a version param on every link to the raw render so
caches cannot serve a stale manuscript behind a fresh wrapper; these
tests lock that contract and the layout it depends on.
"""

from __future__ import annotations

import re
import zlib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
WRAPPER = REPO_ROOT / "dashboard" / "src" / "app" / "paper" / "page.tsx"
WEB = REPO_ROOT / "dashboard" / "public" / "paper" / "web"


def test_wrapper_declares_exactly_one_version() -> None:
    source = WRAPPER.read_text()
    versions = re.findall(r'PAPER_VERSION = "([^"]+)"', source)
    assert len(versions) == 1
    # Every ?v= reference routes through the constant — no hardcoded
    # version strings that could drift from it.
    assert len(re.findall(r"\?v=", source)) == len(
        re.findall(r"\?v=\$\{PAPER_VERSION\}", source)
    )


def test_synced_render_exists_and_carries_the_manuscript() -> None:
    index = WEB / "index.html"
    assert index.exists()
    assert (WEB / "index.pdf").exists()
    assert (WEB / "paper_files").is_dir()
    html = index.read_text()
    assert "How Large Language Models Answer Questions" in html


def test_synced_render_applied_the_project_config() -> None:
    # paper/_quarto.yml supplies the table of contents, section numbers and
    # bibliography. Quarto skips project files whose absolute path contains a
    # dot-directory (such as .claude/worktrees/...), and a render there comes
    # out without all three, with every citation left as a raw @key.
    html = (WEB / "index.html").read_text()
    assert 'id="TOC"' in html
    assert 'id="refs"' in html
    assert html.count('class="header-section-number"') >= 50
    spans = re.findall(r'<span class="citation"[^>]*>(.*?)</span>', html, flags=re.S)
    unresolved = [
        span for span in spans if "@" in re.sub(r"<[^>]+>", "", span) or "???" in span
    ]
    assert spans and unresolved == []


def _inflated_pdf_streams(path: Path) -> bytes:
    data = path.read_bytes()
    chunks = []
    for match in re.finditer(rb"stream\r?\n", data):
        try:
            chunks.append(zlib.decompressobj().decompress(data[match.end() :]))
        except zlib.error:
            continue
    return b"".join(chunks)


def test_synced_pdf_applied_the_project_config() -> None:
    # The PDF counterpart of the check above. A resolved bibliography leaves
    # one cite.ref-* named destination per reference and numbered sections
    # leave section.N destinations; a render without _quarto.yml has neither.
    # Its numbered sections and subsections pair one to one with the HTML's,
    # so a PDF from an older manuscript with a different outline fails too.
    pdf = WEB / "index.pdf"
    assert pdf.read_bytes() == (REPO_ROOT / "paper" / "paper.pdf").read_bytes()
    streams = _inflated_pdf_streams(pdf)
    html = (WEB / "index.html").read_text()
    references = html.count('class="csl-entry"')
    cite_targets = set(re.findall(rb"\(cite\.ref-[^)]+\)", streams))
    assert references > 0 and len(cite_targets) == references
    for level, tag in (("section", "h2"), ("subsection", "h3")):
        targets = set(re.findall(rb"\(" + level.encode() + rb"\.\d[\d.]*\)", streams))
        headings = re.findall(rf'<{tag}[^>]*>\s*<span class="header-section-number"', html)
        assert len(targets) == len(headings) > 0, (level, len(targets), len(headings))


def test_old_pdf_path_keeps_serving() -> None:
    # /ai-beliefs/paper.pdf predates the wrapper and has been shared;
    # next.config redirects it to the synced render.
    config = (REPO_ROOT / "dashboard" / "next.config.ts").read_text()
    assert 'source: "/paper.pdf"' in config
    assert 'destination: "/paper/web/index.pdf"' in config


def test_iframe_contract() -> None:
    source = WRAPPER.read_text()
    assert 'sandbox="allow-same-origin allow-popups allow-popups-to-escape-sandbox"' in source
    assert 'loading="lazy"' in source
    assert "STANDALONE_HREF" in source and "PDF_HREF" in source
