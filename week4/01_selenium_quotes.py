from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.get("https://quotes.toscrape.com/js/")
    for q in driver.find_elements(By.CSS_SELECTOR, "div.quote"):
        print(q.find_element(By.CSS_SELECTOR, "span.text").text,
              "-", q.find_element(By.CSS_SELECTOR, "small.author").text)
finally:
    driver.quit()
