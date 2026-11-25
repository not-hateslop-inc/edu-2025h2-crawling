import requests

r = requests.get("https://books.toscrape.com/", headers={"User-Agent": "hateslop-edu/1.0"}, timeout=10)
print(r.status_code, r.headers.get("content-type"))
print(r.text[:300])
