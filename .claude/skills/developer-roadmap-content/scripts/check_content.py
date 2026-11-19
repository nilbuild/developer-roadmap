#!/usr/bin/env python3
"""Lint and inspect developer-roadmap topic content files.

Files live at roadmaps/<roadmap-slug>/content/<topic-slug>@<node-id>.md.
The rules mirror contributing.md and scripts/sync-repo-to-database.ts in the
repo (that script is what turns these files into what roadmap.sh shows).

Usage:
  check_content.py lint <file-or-dir>... [--json] [--errors-only]
  check_content.py nodes <roadmap-slug> [--repo <path>] [--status missing|ok|stale|all]
  check_content.py fix-order <file-or-dir>... [--dry-run]

`fix-order` only reorders link lines into the allowed type order (a stable
sort, so links of the same type keep their relative order). It changes no
text, URL or whitespace, keeps the file's trailing newline as it was, and
skips any file whose links it can't parse.

`lint` is offline. `nodes` fetches the public roadmap JSON from
https://roadmap.sh/api/v1-official-roadmap/<slug> to list the roadmap's topic
nodes with their IDs, the filename each one should have, and whether the file
exists.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

# Allowed resource types, in the order links should appear. The sync script
# silently turns any other type into "article", so an unknown type is an error.
TYPE_ORDER = ["roadmap", "official", "opensource", "article", "course",
              "podcast", "video", "book", "feed"]
VISIT_LINE = "Visit the following resources to learn more:"
MAX_LINKS = 8
BANNED_DOMAINS = ["geeksforgeeks.org"]
FILENAME_RE = re.compile(r"^(?P<slug>[a-z0-9_-]*)@(?P<id>[A-Za-z0-9_-]+)\.md$")
LINK_RE = re.compile(r"^- \[@(?P<type>[a-z.]+)@(?P<title>.+)\]\((?P<url>[^)\s]+)\)\s*$")
LOOSE_LINK_RE = re.compile(r"^\s*[-*]\s*\[.*\]\(.*\)\s*$")
THIN_CHARS = 120  # a description shorter than this is almost always a stub


def slugify(value: str) -> str:
    """Same as scripts/lib/slugger.ts."""
    return re.sub(r"[^A-Za-z0-9_\- ]", "", value.lower()).strip().replace(" ", "-")


def lint_file(path: Path) -> list[dict]:
    issues: list[dict] = []

    def add(level: str, code: str, msg: str, line: int | None = None):
        issues.append({"file": str(path), "line": line, "level": level,
                       "code": code, "message": msg})

    if "@" not in path.name:
        # index.md and similar are not topics; the sync skips them too.
        add("info", "not-a-topic", "no @<node-id> in the name, so not a topic file; skipped")
        return issues
    m = FILENAME_RE.match(path.name)
    if not m:
        add("error", "filename", "name must be <topic-slug>@<node-id>.md "
            "(lowercase slug of letters, digits, - or _; the slug may be empty "
            "when the label has no letters, e.g. '$?')")
    if path.parent.name != "content":
        add("error", "location", "file must sit in roadmaps/<roadmap-slug>/content/")

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        add("error", "encoding", "file is not valid UTF-8")
        return issues
    lines = text.splitlines()

    if not text.strip():
        add("error", "empty", "file is empty")
        return issues

    # Title
    h1 = [i for i, l in enumerate(lines) if re.match(r"^# \S", l)]
    first = next((i for i, l in enumerate(lines) if l.strip()), 0)
    if not h1:
        add("error", "title", "missing '# Title' heading (the sync needs an H1)", 1)
    else:
        if h1[0] != first:
            add("error", "title", "the '# Title' heading must be the first line", h1[0] + 1)
        if len(h1) > 1:
            add("warning", "title", "more than one '# ' heading", h1[1] + 1)

    # Links
    link_lines = [(i, l) for i, l in enumerate(lines) if LOOSE_LINK_RE.match(l)]
    visit_idx = [i for i, l in enumerate(lines) if l.strip() == VISIT_LINE]
    near_visit = [i for i, l in enumerate(lines)
                  if "following resources" in l.lower() and l.strip() != VISIT_LINE]
    for i in near_visit:
        add("error", "visit-line", f"must read exactly '{VISIT_LINE}'", i + 1)

    links = []
    for i, l in link_lines:
        lm = LINK_RE.match(l)
        if not lm:
            add("error", "link-format",
                "link must look like '- [@type@Title](https://...)'", i + 1)
            continue
        t = lm["type"]
        if t not in TYPE_ORDER:
            add("error", "link-type",
                f"unknown type '@{t}@' (allowed: {', '.join(TYPE_ORDER)}); "
                "the sync would silently file it as an article", i + 1)
        links.append((i, t, lm["title"], lm["url"]))

    if link_lines and not visit_idx:
        add("error", "visit-line",
            f"links present but no '{VISIT_LINE}' line; the sync drops the last "
            "paragraph before the links, so real description text would be lost")
    if visit_idx and not link_lines:
        add("error", "visit-line", f"'{VISIT_LINE}' line with no links under it",
            visit_idx[0] + 1)
    if visit_idx and link_lines and link_lines[0][0] < visit_idx[0]:
        add("error", "visit-line", "links must come after the visit line",
            link_lines[0][0] + 1)
    if link_lines:
        last_link = link_lines[-1][0]
        trailing = [i for i in range(last_link + 1, len(lines)) if lines[i].strip()]
        if trailing:
            add("error", "structure", "nothing should follow the link list",
                trailing[0] + 1)
        blanks = [i for i in range(link_lines[0][0], last_link)
                  if not lines[i].strip()]
        if blanks:
            add("error", "structure", "blank line inside the link list breaks it "
                "into two lists; only one gets synced", blanks[0] + 1)

    if len(links) > MAX_LINKS:
        add("error", "link-count", f"{len(links)} links; the maximum is {MAX_LINKS}")

    ranks = [(i, TYPE_ORDER.index(t)) for i, t, _, _ in links if t in TYPE_ORDER]
    for (i0, r0), (i1, r1) in zip(ranks, ranks[1:]):
        if r1 < r0:
            add("error", "link-order",
                f"'@{TYPE_ORDER[r1]}@' after '@{TYPE_ORDER[r0]}@'; order is "
                + " > ".join(TYPE_ORDER), i1 + 1)
            break

    seen: dict[str, int] = {}
    for i, t, title, url in links:
        low = url.lower()
        if any(d in low for d in BANNED_DOMAINS):
            add("error", "banned-domain", "GeeksforGeeks links are not accepted", i + 1)
        if not low.startswith(("https://", "http://")):
            add("error", "link-url", "URL must be absolute (https://...)", i + 1)
        elif low.startswith("http://"):
            add("warning", "link-url", "use https:// if the site supports it", i + 1)
        key = low.rstrip("/")
        if key in seen:
            add("error", "duplicate-link", f"same URL as line {seen[key]}", i + 1)
        seen.setdefault(key, i + 1)
        if not title.strip():
            add("error", "link-format", "link has no title", i + 1)

    # Description: everything between the title and the visit line / links
    start = (h1[0] + 1) if h1 else 0
    end = visit_idx[0] if visit_idx else (link_lines[0][0] if link_lines else len(lines))
    body = "\n".join(lines[start:end]).strip()
    if not body:
        add("error", "no-description", "no description text under the title")
    elif len(re.sub(r"\s+", " ", body)) < THIN_CHARS:
        add("warning", "thin-description",
            f"description is only {len(body)} characters; aim for a real paragraph")
    if not links and body:
        add("info", "no-links", "topic has no learning resources")

    return issues


def iter_files(targets: list[str]):
    for t in targets:
        p = Path(t)
        if p.is_dir():
            yield from sorted(p.rglob("*.md")) if p.name != "content" else sorted(p.glob("*.md"))
        elif p.suffix == ".md":
            yield p
        else:
            print(f"skipping {t}: not a .md file or directory", file=sys.stderr)


def cmd_lint(args) -> int:
    all_issues = []
    ids: dict = {}
    count = 0
    for f in iter_files(args.paths):
        if "/content/" not in f.as_posix() and f.parent.name != "content":
            continue  # readme.md and other non-topic files
        count += 1
        all_issues += lint_file(f)
        m = FILENAME_RE.match(f.name)
        if m:
            ids.setdefault((f.parent, m["id"]), []).append(f)
    for (_, nid), fs in ids.items():
        if len(fs) > 1:
            for f in fs:
                all_issues.append({"file": str(f), "line": None, "level": "error",
                    "code": "duplicate-node",
                    "message": f"{len(fs)} files share node id {nid}: "
                               + ", ".join(x.name for x in fs)
                               + " (keep the one whose slug matches the node label)"})
    if args.errors_only:
        all_issues = [i for i in all_issues if i["level"] == "error"]
    if args.json:
        print(json.dumps({"files_checked": count, "issues": all_issues}, indent=2))
    else:
        for i in all_issues:
            loc = f"{i['file']}:{i['line']}" if i["line"] else i["file"]
            print(f"{i['level'].upper():7} {i['code']:17} {loc}  {i['message']}")
        by = {}
        for i in all_issues:
            by[i["level"]] = by.get(i["level"], 0) + 1
        files_with = len({i["file"] for i in all_issues if i["level"] == "error"})
        print(f"\nChecked {count} files: {by.get('error', 0)} errors in {files_with} files, "
              f"{by.get('warning', 0)} warnings, {by.get('info', 0)} notes.")
    return 1 if any(i["level"] == "error" for i in all_issues) else 0


def fix_order_file(path: Path, dry: bool) -> str | None:
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    idx = [i for i, l in enumerate(lines) if LOOSE_LINK_RE.match(l)]
    if len(idx) < 2:
        return None
    if idx != list(range(idx[0], idx[-1] + 1)):
        return "skipped: link list is not one contiguous block"
    parsed = [LINK_RE.match(lines[i]) for i in idx]
    if not all(parsed) or any(m["type"] not in TYPE_ORDER for m in parsed):
        return "skipped: has malformed links or unknown types; fix those by hand"
    block = [lines[i] for i in idx]
    new = sorted(block, key=lambda l: TYPE_ORDER.index(LINK_RE.match(l)["type"]))
    if new == block:
        return None
    lines[idx[0]:idx[-1] + 1] = new
    if not dry:
        path.write_text("\n".join(lines), encoding="utf-8")
    return "reordered" + (" (dry run)" if dry else "")


def cmd_fix_order(args) -> int:
    changed = 0
    for f in iter_files(args.paths):
        if "@" not in f.name or f.parent.name != "content":
            continue
        r = fix_order_file(f, args.dry_run)
        if r:
            print(f"{r:12} {f}")
            changed += r.startswith("reordered")
    print(f"\n{changed} files reordered.")
    return 0


def find_repo(start: str | None) -> Path | None:
    p = Path(start or os.getcwd()).resolve()
    for d in [p, *p.parents]:
        if (d / "roadmaps").is_dir() and (d / "contributing.md").exists():
            return d
    return None


def cmd_nodes(args) -> int:
    url = f"https://roadmap.sh/api/v1-official-roadmap/{args.slug}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (compatible; roadmap-content-check/1.0)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    if isinstance(data, dict) and data.get("error"):
        print(f"roadmap.sh error: {data['error']}", file=sys.stderr)
        return 2
    nodes = [n for n in data.get("nodes", []) if n.get("type") in ("topic", "subtopic")]

    repo = find_repo(args.repo)
    content = repo / "roadmaps" / args.slug / "content" if repo else None
    files = {}
    if content and content.is_dir():
        for f in content.glob("*.md"):
            m = FILENAME_RE.match(f.name)
            if m:
                files.setdefault(m["id"], []).append(f.name)

    rows = []
    for n in nodes:
        label = (n.get("data") or {}).get("label", "")
        expected = f"{slugify(label)}@{n['id']}.md"
        have = files.get(n["id"], [])
        if not have:
            status = "missing"
        elif len(have) > 1:
            status = "duplicate"
        else:
            status = "ok" if have[0] == expected else "renamed"
        rows.append({"id": n["id"], "label": label, "type": n.get("type"),
                     "expected_file": expected, "current_files": have, "status": status})
    node_ids = {n["id"] for n in nodes}
    for nid, names in sorted(files.items()):
        if nid not in node_ids:
            rows.append({"id": nid, "label": None, "type": None, "expected_file": None,
                         "current_files": names, "status": "stale"})

    if args.status != "all":
        want = {"missing": {"missing"}, "ok": {"ok"},
                "stale": {"stale", "renamed", "duplicate"}}[args.status]
        rows = [r for r in rows if r["status"] in want]
    if args.json:
        print(json.dumps(rows, indent=2))
    else:
        for r in rows:
            have = ", ".join(r["current_files"]) or "-"
            want = r["expected_file"] or "-"
            extra = "" if r["status"] in ("ok", "missing") else f"   (now: {have})"
            print(f"{r['status']:9} {r['id']:24} {(r['label'] or '-')[:40]:40} {want}{extra}")
        if not content or not content.is_dir():
            print("\n(no local roadmaps/<slug>/content folder found; pass --repo)", file=sys.stderr)
        print(f"\n{len(nodes)} topic nodes on roadmap.sh, "
              f"{sum(len(v) for v in files.values())} topic files locally.",
              file=sys.stderr)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    lp = sub.add_parser("lint", help="check content files offline")
    lp.add_argument("paths", nargs="+")
    lp.add_argument("--json", action="store_true")
    lp.add_argument("--errors-only", action="store_true")
    np_ = sub.add_parser("nodes", help="list a roadmap's topic nodes from roadmap.sh")
    np_.add_argument("slug")
    np_.add_argument("--repo", help="path to the developer-roadmap checkout")
    np_.add_argument("--status", default="all", choices=["all", "missing", "ok", "stale"])
    np_.add_argument("--json", action="store_true")
    fp = sub.add_parser("fix-order", help="reorder links into the allowed type order")
    fp.add_argument("paths", nargs="+")
    fp.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    return {"lint": cmd_lint, "nodes": cmd_nodes, "fix-order": cmd_fix_order}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
