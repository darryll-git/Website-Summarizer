import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import time

class ScrapeWebsite:
    def __init__(self, url):
        self.url = url

        options = uc.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--start-maximized")

        # Add a real browser user-agent
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0.0.0 Safari/537.36"
        )

        driver = uc.Chrome(options=options)

        driver.get(url)
        time.sleep(5)  # Give JS and bot checks time

        page_source = driver.page_source
        driver.quit()

        soup = BeautifulSoup(page_source, "html.parser")
        self.title = soup.title.string if soup.title else "No title found"

        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()

        self.text = soup.body.get_text(separator="\n", strip=True)

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# {self.title}\n\n")
            f.write(self.text)

if __name__ == "__main__":
    url = input("Enter website URL: ")
    scraper = ScrapeWebsite(url)
    scraper.save_to_file("raw_page.md")
    print("✅ Saved scraped content to raw_page.md")
