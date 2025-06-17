# scrapers/nilmamano_dsa.py

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tqdm import tqdm

def extract_title(soup):
    if soup.title:
        return soup.title.text.strip()
    
    h1 = soup.find("h1")
    if h1:
        return h1.text.strip()
    
    return None

def extract_main_content(soup):
    main = soup.find("article")
    if not main:
        main = soup.find("div", {"role": "main"}) or soup.find("div", class_="prose")

    if not main:
        return None

    paragraphs = main.find_all(["p", "h1", "h2", "h3", "ul", "ol", "li"])
    content = "\n\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
    return content.strip()

def scrape_blog_post(url, content_type):
    try:
        res = requests.get(url)
        res.raise_for_status()
    except Exception as e:
        print(f"❌ Failed to fetch {url}: {e}")
        return None

    soup = BeautifulSoup(res.text, "html.parser")
    title = extract_title(soup)
    content = extract_main_content(soup)

    if not title or not content:
        print(f"❌ Failed to parse {url}: No recognizable content or title found.")
        return None

    return {
        "title": title,
        "content": content,
        "content_type": content_type,
        "source_url": url,
        "author": "",
        "user_id": ""
    }

def scrape():
    print("🚀 Scraping Nil Mamano’s DSA Blog Posts...")
    BASE_URL = "https://nilmamano.com"
    DSA_BLOGS_URL = f"{BASE_URL}/blog/category/dsa"

    try:
        response = requests.get(DSA_BLOGS_URL)
        response.raise_for_status()
    except Exception as e:
        print(f"❌ Failed to fetch {DSA_BLOGS_URL}: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article")

    links = set()
    for article in articles:
        a_tag = article.find("a", href=True)
        if a_tag and "/blog/" in a_tag["href"]:
            full_url = urljoin(BASE_URL, a_tag["href"])
            links.add(full_url)

    print(f"✅ Found {len(links)} DSA blog posts.")

    items = []
    for link in tqdm(links, desc="Processing DSA blogs"):
        item = scrape_blog_post(link, "blog")
        if item:
            items.append(item)
    return items
