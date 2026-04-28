"""
Adds doi, google_scholar_id, altmetric={true}, dimensions={true} to papers.bib.
Uses Crossref API for DOIs and scholarly for Google Scholar IDs.
Run from the repo root: python3 scripts/add_paper_metadata.py
"""

import sys
import time
import re
import json
import urllib.request
import urllib.parse

SCHOLAR_ID = "nvzgGIcAAAAJ"
BIB_FILE = "_bibliography/papers.bib"
MAILTO = "tmorstyn@gmail.com"

# ─── helpers ──────────────────────────────────────────────────────────────────

def normalise_title(t):
    return re.sub(r"[^a-z0-9 ]", "", t.lower()).strip()


def crossref_doi(title, first_author_surname, year):
    """Return DOI string (without https://doi.org/) or None."""
    q = urllib.parse.quote(title)
    url = (
        f"https://api.crossref.org/works"
        f"?query.bibliographic={q}"
        f"&query.author={urllib.parse.quote(first_author_surname)}"
        f"&rows=5"
        f"&mailto={MAILTO}"
    )
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            data = json.loads(resp.read())
        items = data.get("message", {}).get("items", [])
        target = normalise_title(title)
        for item in items:
            item_title = item.get("title", [""])[0]
            if not item_title:
                continue
            if normalise_title(item_title) == target:
                # year sanity-check (allow ±1)
                pub_year = None
                for date_field in ("published", "published-print", "published-online"):
                    dp = item.get(date_field, {}).get("date-parts", [[]])
                    if dp and dp[0]:
                        pub_year = dp[0][0]
                        break
                if pub_year and year and abs(int(pub_year) - int(year)) > 1:
                    continue
                return item.get("DOI")
    except Exception as e:
        print(f"    Crossref error for '{title[:60]}': {e}")
    return None


def extract_entries(bib_text):
    """Return list of (key, entry_text_span_start, entry_text_span_end)."""
    entries = []
    for m in re.finditer(r"@\w+\{([^,]+),", bib_text):
        key = m.group(1).strip()
        start = m.start()
        # find matching closing brace
        depth = 0
        pos = start
        while pos < len(bib_text):
            if bib_text[pos] == "{":
                depth += 1
            elif bib_text[pos] == "}":
                depth -= 1
                if depth == 0:
                    entries.append((key, start, pos + 1))
                    break
            pos += 1
    return entries


def get_field(entry_text, field):
    """Extract a field value from a bib entry string."""
    pattern = rf"\b{field}\s*=\s*[{{\"](.*?)[}}\"]"
    m = re.search(pattern, entry_text, re.IGNORECASE | re.DOTALL)
    if m:
        return m.group(1).strip()
    return None


def field_exists(entry_text, field):
    pattern = rf"\b{field}\s*="
    return bool(re.search(pattern, entry_text, re.IGNORECASE))


def insert_fields_before_closing(entry_text, fields_dict):
    """Insert new fields (as dict) before the closing } of an entry."""
    new_lines = []
    for k, v in fields_dict.items():
        new_lines.append(f"  {k}={{{v}}},")
    insertion = "\n".join(new_lines) + "\n"
    last_brace = entry_text.rfind("}")
    # ensure the preceding line ends with a comma
    before = entry_text[:last_brace].rstrip()
    if before and not before.endswith(","):
        before += ","
    return before + "\n" + insertion + entry_text[last_brace:]


# ─── Step 1: fetch Google Scholar IDs (with timeout guard) ────────────────────

scholar_map = {}  # normalised_title -> author_pub_id

import threading

def fetch_scholar():
    try:
        from scholarly import scholarly as sc
        print("Fetching Google Scholar author profile…")
        sys.stdout.flush()
        author = sc.fill(
            sc.search_author_id(SCHOLAR_ID), sections=["publications"]
        )
        print(f"  Found {len(author['publications'])} publications on Scholar")
        for pub in author["publications"]:
            t = pub.get("bib", {}).get("title", "")
            pub_id = pub.get("author_pub_id", "")
            if t and pub_id:
                scholar_map[normalise_title(t)] = pub_id
        print(f"  Mapped {len(scholar_map)} Scholar IDs")
    except Exception as e:
        print(f"  scholarly failed: {e}")
    sys.stdout.flush()

t = threading.Thread(target=fetch_scholar, daemon=True)
t.start()
t.join(timeout=60)
if t.is_alive():
    print("  Scholar fetch timed out after 60s — skipping Scholar IDs, continuing with Crossref")
else:
    print(f"  Scholar done ({len(scholar_map)} IDs mapped)")
sys.stdout.flush()

# ─── Step 2: parse bib file ───────────────────────────────────────────────────

with open(BIB_FILE, encoding="utf-8") as f:
    bib_text = f.read()

entries = extract_entries(bib_text)
print(f"\nParsed {len(entries)} entries from {BIB_FILE}")

# ─── Step 3: for each entry, look up DOI and scholar ID, patch text ───────────

patches = []  # (start, end, new_text)

for i, (key, start, end) in enumerate(entries):
    entry_text = bib_text[start:end]

    title = get_field(entry_text, "title") or ""
    year = get_field(entry_text, "year") or ""
    author_raw = get_field(entry_text, "author") or ""
    first_author = author_raw.split(" and ")[0].split(",")[0].split()[-1].lower() if author_raw else ""

    print(f"[{i+1}/{len(entries)}] {key}")
    sys.stdout.flush()

    to_add = {}

    # Google Scholar ID
    if not field_exists(entry_text, "google_scholar_id"):
        norm = normalise_title(title)
        if norm in scholar_map:
            to_add["google_scholar_id"] = scholar_map[norm]

    # DOI
    doi_needed = not field_exists(entry_text, "doi")
    doi = None
    if doi_needed and title:
        doi = crossref_doi(title, first_author, year)
        if doi:
            to_add["doi"] = doi
            print(f"  doi: {doi}")
        else:
            print(f"  doi: not found")
        time.sleep(0.2)  # polite rate limiting

    # altmetric + dimensions (only if we have a doi, either new or existing)
    has_doi = not doi_needed or doi
    if has_doi:
        if not field_exists(entry_text, "altmetric"):
            to_add["altmetric"] = "true"
        if not field_exists(entry_text, "dimensions"):
            to_add["dimensions"] = "true"

    if to_add:
        new_entry = insert_fields_before_closing(entry_text, to_add)
        patches.append((start, end, new_entry))

# ─── Step 4: apply patches in reverse order so positions stay valid ───────────

patches.sort(key=lambda x: x[0], reverse=True)
result = bib_text
for start, end, new_text in patches:
    result = result[:start] + new_text + result[end:]

with open(BIB_FILE, "w", encoding="utf-8") as f:
    f.write(result)

print(f"\nDone. {len(patches)} entries updated.")
