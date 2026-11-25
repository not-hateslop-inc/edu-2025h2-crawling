import time
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

BASE = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
RATING = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

def parse_page(url):
    soup = BeautifulSoup(requests.get(url, timeout=10).text, "lxml")
    rows = []
    for card in soup.select("article.product_pod"):
        a = card.select_one("h3 a")
        rows.append({
            "title": a["title"],
            "price": card.select_one("p.price_color").text.strip(),
            "rating": RATING[card.select_one("p.star-rating")["class"][1]],
            "url": urljoin(url, a["href"]),
        })
    nxt = soup.select_one("li.next a")
    return rows, (urljoin(url, nxt["href"]) if nxt else None)

def crawl(start=BASE):
    url, out = start, []
    while url:
        rows, url = parse_page(url)
        out += rows
        time.sleep(1)          # 요청 간격
    return out

if __name__ == "__main__":
    books = crawl()
    print(len(books), books[0])
