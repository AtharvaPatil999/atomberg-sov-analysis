import json
import re
import pandas as pd
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

BRANDS = ["Atomberg", "Crompton", "Havells", "Orient", "Usha"]

def load_json(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def detect_brand(text):
    for brand in BRANDS:
        if re.search(brand, text, re.IGNORECASE):
            return brand
    return "Other"

def sentiment_score(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    return score["compound"]

def analyze_google():
    data = load_json("../data/google_30.json")
    rows = []
    for item in data:
        title = item.get("title", "")
        snippet = item.get("snippet", "")
        link = item.get("link", "")
        text = f"{title} {snippet}"
        brand = detect_brand(text)
        sentiment = sentiment_score(text)
        rows.append({"source": "Google", "brand": brand, "text": text, "sentiment": sentiment, "link": link})
    return pd.DataFrame(rows)

def analyze_youtube():
    data = load_json("../data/youtube_30.json")
    rows = []
    for item in data:
        title = item.get("title", "")
        desc = item.get("descriptionSnippet", "")
        views = item.get("viewCount", {}).get("text", "0")
        text = f"{title} {desc}"
        brand = detect_brand(text)
        sentiment = sentiment_score(text)
        rows.append({"source": "YouTube", "brand": brand, "text": text, "sentiment": sentiment, "views": views})
    return pd.DataFrame(rows)

if __name__ == "__main__":
    google_df = analyze_google()
    yt_df = analyze_youtube()
    df = pd.concat([google_df, yt_df], ignore_index=True)

    df.to_csv("../results/analysis.csv", index=False)
    print(" Analysis saved to ../results/analysis.csv")

    summary = df.groupby("brand").size()
    print("\n Share of Voice (count of mentions):")
    print(summary)

    summary.plot(kind="bar", title="Share of Voice")
    plt.savefig("../results/sov_chart.png")
    plt.show()
