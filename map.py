from requests import get
from time import sleep

# List of Wikipedia language codes you want to train your model for
languages = ["en"]
url_template = "https://{lang}.wikipedia.org/wiki/Special:AllPages"

OUTPUT_FILE = "pageID.py"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/117.0.0.0 Safari/537.36 PythonWikipediaBot/1.0"
    )
}

def get_all_titles(lang):
    titles = []
    url = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "allpages",
        "aplimit": "max",  # maximum allowed
        "format": "json"
    }

    while True:
        response = get(url, headers=HEADERS, params=params)
        if response.status_code != 200:
            print(f"Failed to fetch {lang} Wikipedia: {response.status_code}")
            break
        else:
            print("fetch successful")
        data = response.json()
        print(data)
        pages = data.get("query", {}).get("allpages", [])
        for page in pages:
            titles.append(f"{lang}@{page["pageid"]}")
        # Check if there's a continuation token
        if "continue" in data:
            params.update(data["continue"])
        else:
            break

        sleep(1)  # Respect rate limiting

    return titles

all_titles = []

for lang in languages:
    print(f"Fetching titles for language: {lang}")
    titles = get_all_titles(lang)
    print(f"Found {len(titles)} pages in {lang}")
    all_titles.extend(titles)

# Save all titles to a python file
all_titles=set(all_titles)
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("page_id=[")
    for title in all_titles:
        f.write(f'"{title}",')
    f.write("]")

print(f"Done! Total pages collected: {len(all_titles)}")
print(f"Titles saved to {OUTPUT_FILE}")
