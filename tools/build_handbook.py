#!/usr/bin/env python3
"""Build the local reading copy and check its Markdown file references."""
from pathlib import Path
import json
import re
from urllib.parse import urlsplit, unquote
import os

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS = [
    "guides/00-start-here.md",
    "research/market-foundations.md",
    "guides/00-common-settings.md",
    "guides/web-platform.md",
    *[str(p.relative_to(ROOT)) for p in sorted((ROOT / "guides").glob("[0-9][0-9]-*.md"))
      if not p.name.startswith("00-") and not p.name.startswith("15-")],
    "research/web-desktop-differences.md",
    "guides/web-option-net-flow.md",
    "guides/web-dynamic-walls.md",
    "guides/web-market-maker-pressure.md",
    "guides/web-market-maker-sentiment.md",
    "guides/web-exhaustion.md",
    "guides/15-workflows-and-risk.md",
    "research/evidence-and-media.md",
    "research/coverage-and-unknowns.md",
]
LINK = re.compile(r"\]\(([^)\n]+)\)")


def rebase(text, source):
    def convert(match):
        target = match.group(1)
        parsed = urlsplit(target.strip("<>"))
        if parsed.scheme or target.startswith("#"):
            return match.group(0)
        path = (source.parent / unquote(parsed.path)).resolve()
        relative = Path(os.path.relpath(path, ROOT)).as_posix()
        if parsed.fragment:
            relative += "#" + parsed.fragment
        return "](" + relative + ")"
    return LINK.sub(convert, text)


parts = [
    "# DeepGamma完整手册\n\n核验日期：2026-10-29。由分篇指南自动合并；"
    "源文件与独立查阅入口见[README](README.md)。所有交易情景为教学假设。\n\n## 阅读目录\n"
]
for index, name in enumerate(CHAPTERS, 1):
    source = ROOT / name
    title = source.read_text().splitlines()[0].lstrip("# ")
    parts.append(f"{index}. [{title}](#{'chapter-' + str(index)})\n")

for index, name in enumerate(CHAPTERS, 1):
    source = ROOT / name
    text = rebase(source.read_text(), source)
    fenced = False
    lines = []
    for line in text.splitlines():
        if line.startswith("```"):
            fenced = not fenced
        if not fenced and line.startswith("#"):
            line = "#" + line
        lines.append(line)
    parts.append(f'\n\n<a id="chapter-{index}"></a>\n\n')
    parts.append(f"源文件：[{name}]({name})\n\n")
    parts.append("\n".join(lines) + "\n")

(ROOT / "DeepGamma完整手册.md").write_text("".join(parts))

errors = []
count = 0
indicator_sources = [
    name for name in CHAPTERS
    if re.match(r"guides/(0[1-9]|1[0-4])-", name)
] + [
    "guides/web-option-net-flow.md", "guides/web-dynamic-walls.md",
    "guides/web-market-maker-pressure.md", "guides/web-market-maker-sentiment.md",
    "guides/web-exhaustion.md",
]
assert len(set(indicator_sources)) == 19
assert all(name in CHAPTERS and (ROOT / name).exists() for name in indicator_sources)
assert all("https://www.deepcharts.com/" in (ROOT / name).read_text() for name in indicator_sources)
book_text = (ROOT / "DeepGamma完整手册.md").read_text()
book_anchors = set(re.findall(r'<a id="([^"]+)"', book_text))
assert all(f"chapter-{n}" in book_anchors for n in range(1, len(CHAPTERS) + 1))
files = sorted(ROOT.rglob("*.md"))
for source in files:
    text = source.read_text()
    for match in LINK.finditer(text):
        target = match.group(1).strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or not parsed.path:
            continue
        count += 1
        path = (source.parent / unquote(parsed.path)).resolve()
        if not path.exists():
            errors.append({"file": str(source.relative_to(ROOT)), "target": target})

report = {
    "checked_date": "2026-10-29",
    "markdown_files_checked": len(files),
    "handbook_chapters": len(CHAPTERS),
    "individual_indicator_guides": len(set(indicator_sources)),
    "handbook_chapter_anchors_checked": len(book_anchors),
    "local_references_checked": count,
    "broken_local_references": errors,
    "characters_in_chapter_sources": sum(len((ROOT / p).read_text()) for p in CHAPTERS),
    "checks": [
        "19 cross-version unique indicators mapped to individual guides",
        "14 desktop indicator guides plus a Web configuration supplement",
        "all local Markdown file and image targets exist",
        "chapter links rebased to the combined handbook directory",
    ],
    "limitations": "Local reference checks do not validate trading performance, external future availability or proprietary algorithms.",
}
(ROOT / "research/validation-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2))
print(json.dumps(report, ensure_ascii=False, indent=2))
if errors:
    raise SystemExit(1)
