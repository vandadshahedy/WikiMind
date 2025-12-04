from requests import get
from time import sleep
from json import dump


def get_plaintext_by_pageid(lang: str, pageid: int) -> str:
    """
    Fetch plain-text content of a Wikipedia page using its page ID.
    """
    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/117.0.0.0 Safari/537.36 PythonWikipediaBot/1.0"
        )
    }
    url = f"https://{lang}.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "prop": "extracts",
        "explaintext": 1,  # plain text only (no HTML or markup)
        "pageids": pageid,  # page ID instead of title
        "format": "json"
    }

    response = get(url, headers=HEADERS, params=params)
    data = response.json()

    # Extract page content
    pages = data["query"]["pages"]
    page = pages[str(pageid)]

    if "extract" in page:
        return page["extract"]
    else:
        return ""  # no content (e.g. redirect, empty page, etc.)


# -----------------------------
# Create training data from your page_id list
# -----------------------------
if __name__ == "__main__":
    from pageID import page_id

    training_data = []

    for entry in page_id:
        # Split "lang@pageid"
        lang, pid = entry.split("@")
        pageid = int(pid)

        print(f"Fetching: {lang} - {pageid}")
        text = get_plaintext_by_pageid(lang, pageid)

        if text:  # Only save non-empty content
            training_data.append({
                "language": lang,
                "pageid": pageid,
                "text": text
            })

        sleep(1)  # Rate limiting

    # Save training data to file
    with open("training_data.json", "w", encoding="utf-8") as f:
        dump(training_data, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(training_data)} training samples")