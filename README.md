Atomberg Share-of-Voice Analysis

This repository provides scripts and analysis for measuring Atomberg’s Share-of-Voice (SoV) on Google and YouTube, comparing brand visibility, engagement, and sentiment against major competitors.

Project Structure:-

scripts folder:- Python scripts for scraping and analysis
  scrape_google.py:- Scrapes top N Google search results for a given query
  scrape_youtube.py:- Scrapes top N YouTube search results
  analyze_sov.py:- Analyzes brand mentions, computes SoV, generates charts

data folder:-JSON/CSV outputs from scraping (sample data only)
results folder:-  Generated charts in (PNG) format and processed CSV results
requirements.txt:-  Contains all Python dependencies/ required libraries


How to Run the ai agent:-

1. Create a virtual environment (optional but recommended)
    run this command "python -m venv venv" (for windows)
2. Activate the environment:
    run this command "venv\Scripts\activate" (for windows)
3. Install dependencies
    run this command "pip install -r requirements.txt" or manually run "pip install pandas numpy requests beautifulsoup4 youtube-search-python snscrape tqdm vaderSentiment textblob matplotlib reportlab"
4. Set your SerpAPI key as an environment variable (or hardcode in scrape_google.py)
   Google search via SerpAPI needs a free API key hence to get one free key .
   Sign up at : "https://serpapi.com/" after signup from dashboard copy the api key and use in "scrape_google.py"
5. Run these files :-
   python scripts/scrape_google.py "smart fan" 30
   python scripts/scrape_youtube.py "smart fan" 30  
   python scripts/analyze_sov.py
6. Check data folder and results folder for outputs and charts

****Notes****
  * This repository demonstrates a Python-based implementation for scraping, analyzing, and visualizing Atomberg's Share-of-Voice (SoV). 
  * While the same workflow can be automated using low-code tools like **n8n**, we used Python to compute metrics, generate charts, and perform competitor analysis for greater control and flexibility.
  * Analysis is based on publicly available data only.


