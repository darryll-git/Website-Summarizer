# Webpage Scraper → Cleaner → Summarizer

This project is a **three-stage pipeline** for extracting and summarizing the main content from any webpage, including JavaScript-heavy sites.  
It uses:

1. **Selenium / BeautifulSoup** – to scrape webpage content into `.md` format.
2. **Regex Cleaning** – to remove menus, ads, footers, market tickers, timestamps, and other unwanted elements.
3. **OpenAI API** – to summarize the cleaned text into a concise, human-readable summary.

## 🛠 Requirements

Install dependencies with:

```bash
pip install selenium beautifulsoup4 webdriver-manager undetected-chromedriver python-dotenv openai
