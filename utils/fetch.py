# utils/fetch.py

import requests

def fetch_url(url, timeout=10):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/114.0.0.0 Safari/537.36"
        )
    }
    res = requests.get(url, headers=headers, timeout=timeout)
    res.raise_for_status()
    return res
