import os
import sys
import json
from serpapi import GoogleSearch

# 🔹 Option 1: Hardcode your key here (replace with your real key)
HARDCODED_API_KEY = "_YOUR_SERP_API_KEY"

def scrape_google(query, num_results=20, api_key=None):
    if api_key is None:
        # Try reading from environment variable, else fallback to hardcoded key
        api_key = os.getenv("SERPAPI_KEY", HARDCODED_API_KEY)

    if not api_key:
        print(" API key missing. Please set SERPAPI_KEY or update HARDCODED_API_KEY in script.")
        sys.exit(1)

    search = GoogleSearch({
        "q": query,
        "num": num_results,
        "api_key": api_key
    })
    results = search.get_dict()

    organic = results.get("organic_results", [])
    output_file = f"../data/google_{num_results}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(organic, f, indent=2, ensure_ascii=False)

    print(f" Saved {len(organic)} Google results to {output_file}")

if __name__ == "__main__":
    # Example run: python scrape_google.py "smart fan" 30
    query = sys.argv[1] if len(sys.argv) > 1 else "smart fan"
    num = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    scrape_google(query, num)
