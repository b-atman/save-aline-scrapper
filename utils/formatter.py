# utils/formatter.py

def format_item(title, content, content_type, source_url=None, author="", user_id=""):
    return {
        "title": title,
        "content": content,
        "content_type": content_type,
        "source_url": source_url,
        "author": author,
        "user_id": user_id
    }
