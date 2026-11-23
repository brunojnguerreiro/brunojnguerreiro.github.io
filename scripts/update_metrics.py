#!/usr/bin/env python3
"""Update the metrics table in content/pages/publications.md.

- Web of Science, Scopus and Google Scholar: read from the CV repository
  (utils/bibliometrics.tex), where they are kept by hand.
- OpenAlex and Semantic Scholar: fetched from their public APIs.

The table is written between the markers
    <!-- metrics:start --> and <!-- metrics:end -->
If an API call fails, the previous row for that source is kept.

Usage:
    python3 scripts/update_metrics.py [--cv PATH_TO_CV_REPO]
"""
import argparse
import datetime
import json
import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGE = ROOT / "content" / "pages" / "publications.md"
DEFAULT_CV = ROOT.parent / "CurriculumVitaeRepo"

ORCID = "0000-0002-4511-5114"
SEMANTIC_SCHOLAR_ID = "2519328"

LINKS = {
    "Web of Science": "https://www.webofscience.com/wos/author/record/C-1257-2008",
    "Scopus": "https://www.scopus.com/authid/detail.uri?authorId=24780644000",
    "Google Scholar": "https://scholar.google.pt/citations?user=TdFhrtAAAAAJ",
    "OpenAlex": f"https://openalex.org/authors/orcid:{ORCID}",
    "Semantic Scholar": f"https://www.semanticscholar.org/author/{SEMANTIC_SCHOLAR_ID}",
}
MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
START, END = "<!-- metrics:start -->", "<!-- metrics:end -->"


def read_cv(cv_dir):
    tex = (cv_dir / "utils" / "bibliometrics.tex").read_text(encoding="utf-8")
    macros = dict(re.findall(r"\\newcommand\{\\(CV\w+)\}\{(\d+)\}", tex))
    rows = {}
    for name, key in (("Web of Science", "WoS"), ("Scopus", "Scopus"),
                      ("Google Scholar", "Scholar")):
        rows[name] = (macros[f"CVnDocs{key}"], macros[f"CVnCites{key}"],
                      macros[f"CVhindex{key}"])
    return rows


def get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "site-metrics-script/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def fetch_apis():
    rows = {}
    try:
        d = get_json(f"https://api.openalex.org/authors/orcid:{ORCID}")
        rows["OpenAlex"] = (str(d["works_count"]), str(d["cited_by_count"]),
                            str(d["summary_stats"]["h_index"]))
    except Exception as e:  # keep the previous row
        print(f"OpenAlex: failed ({e}), keeping previous values", file=sys.stderr)
    try:
        d = get_json(f"https://api.semanticscholar.org/graph/v1/author/"
                     f"{SEMANTIC_SCHOLAR_ID}?fields=paperCount,citationCount,hIndex")
        rows["Semantic Scholar"] = (str(d["paperCount"]), str(d["citationCount"]),
                                    str(d["hIndex"]))
    except Exception as e:
        print(f"Semantic Scholar: failed ({e}), keeping previous values", file=sys.stderr)
    return rows


def previous_rows(page):
    rows = {}
    for name in LINKS:
        m = re.search(r"^\| \[" + re.escape(name) + r"\]\([^)]*\) \| (\d+) \| (\d+) \| (\d+) \|$",
                      page, re.M)
        if m:
            rows[name] = tuple(g.strip() for g in m.groups())
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cv", type=pathlib.Path, default=DEFAULT_CV,
                    help="path to the CV repository (default: %(default)s)")
    args = ap.parse_args()

    page = PAGE.read_text(encoding="utf-8")
    if START not in page or END not in page:
        sys.exit(f"Markers {START} / {END} not found in {PAGE}")

    t = datetime.date.today()
    today = f"{MONTHS[t.month - 1]} {t.year}"
    rows = previous_rows(page)
    rows.update(read_cv(args.cv))
    rows.update(fetch_apis())

    lines = [f"Last updated: {today}.", "",
             "| Source | Documents | Citations | h-index |",
             "|---|---:|---:|---:|"]
    for name in LINKS:
        if name in rows:
            docs, cites, h = rows[name][:3]
            lines.append(f"| [{name}]({LINKS[name]}) | {docs} | {cites} | {h} |")
    table = "\n".join(lines)

    new = re.sub(re.escape(START) + r".*?" + re.escape(END),
                 lambda _: f"{START}\n{table}\n{END}", page, flags=re.S)
    PAGE.write_text(new, encoding="utf-8")
    print(table)


if __name__ == "__main__":
    main()
