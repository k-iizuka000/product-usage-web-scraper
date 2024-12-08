import requests
import pandas as pd
import argparse

def main():
    parser = argparse.ArgumentParser(description="Google Custom Search Script")
    parser.add_argument("--api_key", required=True, help="Google Custom Search API key")
    parser.add_argument("--cx", required=True, help="Custom Search Engine ID")
    parser.add_argument("--query", required=True, help="Search query")

    args = parser.parse_args()

    API_KEY = args.api_key
    CX = args.cx
    query = args.query

    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": API_KEY,
        "cx": CX,
        "q": query,
        "hl": "ja",
        "lr": "lang_ja"
    }

    response = requests.get(url, params=params)
    data = response.json()

    items = data.get("items", [])
    results = []
    for item in items:
        title = item.get("title")
        link = item.get("link")
        snippet = item.get("snippet")
        results.append({
            "Title": title,
            "URL": link,
            "Description": snippet
        })

    df = pd.DataFrame(results)
    df.to_excel("search_results.xlsx", index=False)

if __name__ == "__main__":
    main()
