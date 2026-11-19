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
# The PDF needs the same config: resolved references leave cite.ref-* link
# targets and numbered sections leave section.N targets.
python3 - <<'PY'
import re, sys, zlib
data = open("paper/paper.pdf", "rb").read()
streams = b""
for match in re.finditer(rb"stream\r?\n", data):
    try:
        streams += zlib.decompressobj().decompress(data[match.end():])
    except zlib.error:
        pass
cites = set(re.findall(rb"\(cite\.ref-[^)]+\)", streams))
sections = set(re.findall(rb"\(section\.\d[\d.]*\)", streams))
references = open("paper/paper.html").read().count('class="csl-entry"')
if not (references and len(cites) == references and len(sections) >= 8):
    sys.exit(
        f"paper/paper.pdf has {len(cites)} reference targets for {references} references and "
        f"{len(sections)} section targets: the PDF render did not apply paper/_quarto.yml"
    )
PY
mkdir -p dashboard/public/paper/web
cp paper/paper.html dashboard/public/paper/web/index.html
cp paper/paper.pdf dashboard/public/paper/web/index.pdf
rsync -a --delete paper/paper_files/ dashboard/public/paper/web/paper_files/
echo "synced render into dashboard/public/paper/web/"
