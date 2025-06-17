# scrapers/interviewing_io_blog.py

from bs4 import BeautifulSoup
from markdownify import markdownify as md
from tqdm import tqdm
from utils.fetch import fetch_url
from utils.formatter import format_item

BASE_URL = "https://interviewing.io"
BLOG_URL = f"{BASE_URL}/blog"

def fetch_blog_links():
    print("🔎 Collecting blog URLs from all pages...")
    blog_urls = set()
    page = 1

    while True:
        url = f"{BLOG_URL}/page/{page}" if page > 1 else BLOG_URL
        try:
            res = fetch_url(url)
        except Exception as e:
            print(f"❌ Failed to fetch {url}: {e}")
            break

        soup = BeautifulSoup(res.text, "lxml")
        links = soup.select("a[href^='/blog/']")
        new_links = 0

        for link in links:
            href = link['href']
            if (
                href.startswith("/blog/")
                and not any(x in href for x in ["/page/", "/category/"])
                and len(href.strip("/").split("/")) > 1
            ):
                full_url = BASE_URL + href
                if full_url not in blog_urls:
                    blog_urls.add(full_url)
                    new_links += 1

        if new_links == 0:
            break
        page += 1

    print(f"✅ Found {len(blog_urls)} blog post URLs.")
    return list(blog_urls)

def parse_blog(url):
    try:
        res = fetch_url(url)
        soup = BeautifulSoup(res.text, "lxml")

        title_tag = soup.find("h1")
        title = title_tag.text.strip() if title_tag else "Untitled"

        content_tag = (
            soup.find("div", class_="leading-7") or
            soup.find("article") or
            soup.find("main") or
            soup.find("section") or
            soup.find("div", class_="post-content") or
            soup.find("div", class_="post-body") or
            soup.find("div", class_="prose") or
            soup.find("div", class_="max-w-6xl") or
            soup.select_one("div.mx-auto.flex.max-w-full.flex-col.px-5")
        )

        if not content_tag:
            print(f"⚠️ Failed to extract content from: {url}")
            return None

        markdown_content = md(str(content_tag))

        return format_item(
            title=title,
            content=markdown_content,
            content_type="blog",
            source_url=url
        )
    except Exception as e:
        print(f"❌ Error parsing blog at {url}: {e}")
        return None

def scrape():
    print("🚀 Scraping Interviewing.io Blog...")
    items = []
    blog_urls = fetch_blog_links()

    for url in tqdm(blog_urls, desc="Processing blog posts"):
        item = parse_blog(url)
        if item:
            items.append(item)
        else:
            print(f"❌ Skipped: {url}")

    return items
