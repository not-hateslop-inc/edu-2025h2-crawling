import pandas as pd
from importlib import import_module

crawl = import_module("02_bs4_books").crawl
df = pd.DataFrame(crawl())
df.to_csv("travel_books.csv", index=False, encoding="utf-8-sig")
print(df.head())
