"""
Fetches publications from Google Scholar and writes them to _bibliography/papers.bib.
Retries with backoff when rate-limited.
"""

import sys
import time
from scholarly import scholarly

SCHOLAR_ID = "nvzgGIcAAAAJ"
OUTPUT_FILE = "_bibliography/papers.bib"
MAX_RETRIES = 5

def fetch_with_retry(fn, label):
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            return fn()
        except Exception as e:
            wait = 30 * attempt
            print(f"  Attempt {attempt}/{MAX_RETRIES} failed for '{label}': {e}")
            if attempt < MAX_RETRIES:
                print(f"  Waiting {wait}s before retry...")
                sys.stdout.flush()
                time.sleep(wait)
            else:
                print(f"  Giving up on '{label}'")
                sys.stdout.flush()
                return None

print("Fetching author profile...")
sys.stdout.flush()

author = fetch_with_retry(
    lambda: scholarly.fill(scholarly.search_author_id(SCHOLAR_ID), sections=["publications"]),
    "author profile"
)
if not author:
    sys.exit(1)

print(f"Found {len(author['publications'])} publications")
sys.stdout.flush()

bibtex_entries = []
for i, pub in enumerate(author["publications"]):
    title = pub.get("bib", {}).get("title", "unknown")
    print(f"[{i+1}/{len(author['publications'])}] Fetching: {title}")
    sys.stdout.flush()

    filled = fetch_with_retry(lambda p=pub: scholarly.fill(p), title)
    if not filled:
        continue

    bib_data = filled.get("bib", {})
    if "ENTRYTYPE" not in bib_data:
        bib_data["ENTRYTYPE"] = "article"
    if "ID" not in bib_data:
        author_key = bib_data.get("author", "unknown").split()[0].lower().strip(",")
        year_key = bib_data.get("pub_year", "0000")
        title_key = bib_data.get("title", "untitled").split()[0].lower()
        bib_data["ID"] = f"{author_key}{year_key}{title_key}"

    try:
        bib = scholarly.bibtex(filled)
        bibtex_entries.append(bib)
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write("\n\n".join(bibtex_entries) + "\n")
    except Exception as e:
        print(f"  Warning: could not convert to bibtex: {e}")
        sys.stdout.flush()

    time.sleep(5)

print(f"\nDone. Wrote {len(bibtex_entries)} publications to {OUTPUT_FILE}")
