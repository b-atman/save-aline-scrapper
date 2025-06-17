import os
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
        return text.strip()
    except Exception as e:
        print(f"❌ Failed to read {pdf_path}: {e}")
        return None

def scrape():
    print("📚 Parsing Nil Mamano’s Book (First 7 Chapters)...")
    pdf_path = os.path.join("data", "Nil_book.pdf")
    
    text = extract_text_from_pdf(pdf_path)
    if not text:
        return []

    return [{
        "title": "Sneak Peek: Beyond CTCI - First 7 Chapters",
        "content": text,
        "content_type": "book",
        "source_url": "",
        "author": "Nil Mamano",
        "user_id": ""
    }]
