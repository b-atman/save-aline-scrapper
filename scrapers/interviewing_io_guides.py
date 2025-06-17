# scrapers/interviewing_io_guides.py

from bs4 import BeautifulSoup
from markdownify import markdownify as md
from tqdm import tqdm
from urllib.parse import urljoin
from utils.fetch import fetch_url
from utils.formatter import format_item

BASE_URL = "https://interviewing.io"

def get_company_guide_links():
    print("🔍 Collecting company guide links...")
    links = set()
    try:
        res = fetch_url(BASE_URL + "/topics#companies")
        soup = BeautifulSoup(res.text, "lxml")
        cards = soup.select("a")

        for a in cards:
            href = a.get("href", "")
            text = a.get_text(strip=True)
            if "Interview process" in text and href.startswith("/"):
                full_url = urljoin(BASE_URL, href)
                links.add(full_url)

    except Exception as e:
        print(f"❌ Failed to fetch guide list: {e}")

    print(f"✅ Found {len(links)} company guides.")
    return list(links)

def parse_company_guide(url):
    try:
        res = fetch_url(url)
        soup = BeautifulSoup(res.text, "lxml")

        # Title
        title_tag = soup.find("h1")
        title = title_tag.get_text(strip=True) if title_tag else "Untitled"

        # Main content fallback
        content_tag = (
            soup.find("div", class_="leading-7") or
            soup.find("article") or
            soup.find("main") or
            soup.find("section") or
            soup.find("div", class_="prose") or
            soup.select_one("div[class*='content']") or
            soup.select_one("div[class*='max-w']")
        )

        if not content_tag:
            print(f"⚠️ Failed to extract content from: {url}")
            return None

        markdown_content = md(str(content_tag))

        return format_item(
            title=title,
            content=markdown_content,
            content_type="other",  # or "blog" if preferred
            source_url=url
        )

    except Exception as e:
        print(f"❌ Error parsing guide at {url}: {e}")
        return None

def scrape():
    print("🚀 Scraping Interviewing.io Company Guides...")
    items = []
    guide_links = get_company_guide_links()

    for url in tqdm(guide_links, desc="Processing company guides"):
        item = parse_company_guide(url)
        if item:
            items.append(item)
        else:
            print(f"❌ Skipped: {url}")

    return items
