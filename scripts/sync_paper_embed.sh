#!/bin/bash
# Sync the rendered manuscript into the /paper wrapper's web/ directory.
# Run after `quarto render paper/paper.qmd` (HTML and PDF), then bump
# PAPER_VERSION in dashboard/src/app/paper/page.tsx.
set -euo pipefail
cd "$(dirname "$0")/.."
# Refuse a render that missed paper/_quarto.yml (TOC, section numbers,
# bibliography). Quarto skips project files under a dot-directory, so render
# from a path with no "/." component.
for marker in 'id="TOC"' 'id="refs"' 'class="header-section-number"'; do
  if ! grep -q "$marker" paper/paper.html; then
    echo "paper/paper.html lacks $marker: the render did not apply paper/_quarto.yml" >&2
    exit 1
  fi
done
# The PDF needs the same config and must come from the same manuscript:
# resolved references leave one cite.ref-* link target per reference, and its
# numbered sections and subsections pair one to one with the HTML's.
for output in paper/paper.html paper/paper.pdf; do
  if [ ! "$output" -nt paper/paper.qmd ]; then
    echo "$output is older than paper/paper.qmd: render again before syncing" >&2
    exit 1
  fi
done
python3 - <<'PY'
import re, sys, zlib
data = open("paper/paper.pdf", "rb").read()
html = open("paper/paper.html").read()
streams = b""
for match in re.finditer(rb"stream\r?\n", data):
    try:
        streams += zlib.decompressobj().decompress(data[match.end():])
    except zlib.error:
        pass
cites = set(re.findall(rb"\(cite\.ref-[^)]+\)", streams))
references = html.count('class="csl-entry"')
problems = []
if not (references and len(cites) == references):
    problems.append(f"{len(cites)} reference targets for {references} references")
for level, tag in (("section", "h2"), ("subsection", "h3")):
    targets = set(re.findall(rb"\(" + level.encode() + rb"\.\d[\d.]*\)", streams))
    headings = re.findall(rf'<{tag}[^>]*>\s*<span class="header-section-number"', html)
    if not len(targets) == len(headings) > 0:
        problems.append(f"{len(targets)} {level} targets for {len(headings)} numbered {tag} headings")
if problems:
    sys.exit("paper/paper.pdf does not match paper/paper.html: " + "; ".join(problems))
PY
mkdir -p dashboard/public/paper/web
cp paper/paper.html dashboard/public/paper/web/index.html
cp paper/paper.pdf dashboard/public/paper/web/index.pdf
rsync -a --delete paper/paper_files/ dashboard/public/paper/web/paper_files/
echo "synced render into dashboard/public/paper/web/"
