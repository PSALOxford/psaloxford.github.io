"""
Adds google_scholar_id to papers.bib entries by matching titles to the
author's Google Scholar profile. Run from repo root.
"""

import re
import sys
import signal

SCHOLAR_ID = "nvzgGIcAAAAJ"
BIB_FILE = "_bibliography/papers.bib"


def normalise(t):
    return re.sub(r"[^a-z0-9 ]", "", t.lower()).strip()


def field_exists(entry_text, field):
    return bool(re.search(rf"\b{field}\s*=", entry_text, re.IGNORECASE))


def insert_before_closing(entry_text, field, value):
    last = entry_text.rfind("}")
    before = entry_text[:last].rstrip()
    if before and not before.endswith(","):
        before += ","
    return before + f"\n  {field}={{{value}}},\n" + entry_text[last:]


# ── fetch Scholar IDs ─────────────────────────────────────────────────────────

def timeout_handler(sig, frame):
    raise TimeoutError("Scholar fetch timed out")

signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(120)  # 2 minute hard limit

print("Fetching author profile from Google Scholar…")
sys.stdout.flush()

try:
    from scholarly import scholarly
    author = scholarly.fill(
        scholarly.search_author_id(SCHOLAR_ID),
        sections=["publications"]
    )
    signal.alarm(0)  # cancel alarm
    print(f"Found {len(author['publications'])} publications")
    sys.stdout.flush()
except TimeoutError as e:
    print(f"Timed out: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

scholar_map = {}  # normalised_title -> author_pub_id
for pub in author["publications"]:
    t = pub.get("bib", {}).get("title", "")
    pub_id = pub.get("author_pub_id", "")
    if t and pub_id:
        scholar_map[normalise(t)] = pub_id

print(f"Mapped {len(scholar_map)} Scholar IDs")
sys.stdout.flush()

# ── parse and patch bib file ──────────────────────────────────────────────────

with open(BIB_FILE, encoding="utf-8") as f:
    bib_text = f.read()

entries = []
for m in re.finditer(r"@\w+\{([^,]+),", bib_text):
    key = m.group(1).strip()
    start = m.start()
    depth, pos = 0, start
    while pos < len(bib_text):
        if bib_text[pos] == "{":
            depth += 1
        elif bib_text[pos] == "}":
            depth -= 1
            if depth == 0:
                entries.append((key, start, pos + 1))
                break
        pos += 1

patches = []
matched = 0
for key, start, end in entries:
    entry_text = bib_text[start:end]
    if field_exists(entry_text, "google_scholar_id"):
        continue
    title_m = re.search(r"\btitle\s*=\s*[{\"](.*?)[}\"]", entry_text, re.IGNORECASE | re.DOTALL)
    if not title_m:
        continue
    norm = normalise(title_m.group(1))
    if norm in scholar_map:
        pub_id = scholar_map[norm]
        new_entry = insert_before_closing(entry_text, "google_scholar_id", pub_id)
        patches.append((start, end, new_entry))
        matched += 1
        print(f"  {key}: {pub_id}")

patches.sort(key=lambda x: x[0], reverse=True)
result = bib_text
for start, end, new_text in patches:
    result = result[:start] + new_text + result[end:]

with open(BIB_FILE, "w", encoding="utf-8") as f:
    f.write(result)

print(f"\nDone. Added google_scholar_id to {matched} entries.")
