from scrapers import (
    interviewing_io_blog,
    interviewing_io_guides,
    interviewing_io_interview_guides,
    nilmamano_dsa,
    nil_book
)
import json

def main():
    all_items = []

    print("\n📝 Scraping Interviewing.io Blog...")
    all_items.extend(interviewing_io_blog.scrape())

    print("\n🏢 Scraping Company Guides...")
    all_items.extend(interviewing_io_guides.scrape())

    print("\n📘 Scraping Interview Guides...")
    all_items.extend(interviewing_io_interview_guides.scrape())

    print("\n🧠 Scraping Nil Mamano DSA Blogs...")
    all_items.extend(nilmamano_dsa.scrape())
    
    print("\n📗 Parsing Nil's Book...")
    all_items.extend(nil_book.scrape())


    with open("output.json", "w", encoding="utf-8") as f:
        json.dump({
            "team_id": "aline123",
            "items": all_items
        }, f, indent=2, ensure_ascii=False)

    print(f"\n💾 All items saved to output.json ({len(all_items)} total).")

if __name__ == "__main__":
    main()
