import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urlparse

class WebCrawler:
    def __init__(self):
        self.visited_urls = set()

    def crawl(self, url, depth=2, delay=1):
        if depth == 0 or url in self.visited_urls:
            return

        if not self.is_allowed_by_robots(url):
            print(f"Skipping {url} due to robots.txt rules")
            return

        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                self.index_page(url, soup)
                self.visited_urls.add(url)

                for link in soup.find_all('a'):
                    new_url = link.get('href')
                    if new_url and new_url.startswith('http'):
                        time.sleep(delay)
                        self.crawl(new_url, depth - 1, delay)

        except Exception as e:
            print(f"Error crawling {url}: {e}")

    def is_allowed_by_robots(self, url):
        parsed = urlparse(url)
        robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"

        try:
            response = requests.get(robots_url)
            if response.status_code == 200 and "Disallow: /" in response.text:
                return False
        except:
            pass

        return True

    def index_page(self, url, soup):
        title = soup.title.string if soup.title else "No title"
        paragraph = soup.find('p').get_text() if soup.find('p') else "No paragraph found"

        print(f"\nIndexing: {url}")
        print(f"Title: {title}")
        print(f"First Paragraph: {paragraph}")
        print("-" * 40)

if __name__ == "__main__":
    crawler = WebCrawler()
    crawler.crawl("https://www.example.org")
