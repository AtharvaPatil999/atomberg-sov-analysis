import json
from youtubesearchpython import VideosSearch

def scrape_youtube(query="smart fan", num_results=20):
    videos_search = VideosSearch(query, limit=num_results)
    results = videos_search.result()["result"]

    output_file = f"../data/youtube_{num_results}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f" Saved {len(results)} YouTube results to {output_file}")

if __name__ == "__main__":
    scrape_youtube("smart fan", 30)
