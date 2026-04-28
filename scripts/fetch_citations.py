"""
Fetches citation counts from Google Scholar and writes _data/citations.yml.
Run from repo root: python3 scripts/fetch_citations.py
"""

import signal
import sys
import yaml
from datetime import date

SCHOLAR_ID = "nvzgGIcAAAAJ"
OUTPUT_FILE = "_data/citations.yml"


def timeout_handler(sig, frame):
    raise TimeoutError("Scholar fetch timed out")


signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(120)

print("Fetching author profile from Google Scholar...")
sys.stdout.flush()

try:
    from scholarly import scholarly
    author = scholarly.fill(
        scholarly.search_author_id(SCHOLAR_ID),
        sections=["publications"]
    )
    signal.alarm(0)
    print(f"Found {len(author['publications'])} publications")
    sys.stdout.flush()
except TimeoutError as e:
    print(f"Timed out: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

papers = {}
for pub in author["publications"]:
    pub_id = pub.get("author_pub_id", "")
    title = pub.get("bib", {}).get("title", "")
    year = pub.get("bib", {}).get("pub_year", "Unknown Year")
    citations = pub.get("num_citations", 0)
    if pub_id:
        key = f"{SCHOLAR_ID}:{pub_id}"
        papers[key] = {"citations": citations, "title": title, "year": str(year)}
        print(f"  {citations:4d}  {title[:60]}")

data = {
    "metadata": {"last_updated": str(date.today())},
    "papers": papers,
}

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

print(f"\nDone. Wrote {len(papers)} entries to {OUTPUT_FILE}")
