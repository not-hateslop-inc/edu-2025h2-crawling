import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
rows = []
try:
    driver.get("https://quotes.toscrape.com/js/")
    for _ in range(3):   # 3페이지만
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.quote")))
        rows += [q.find_element(By.CSS_SELECTOR, "span.text").text
                 for q in driver.find_elements(By.CSS_SELECTOR, "div.quote")]
        nxt = driver.find_elements(By.CSS_SELECTOR, "li.next a")
        if not nxt:
            break
        nxt[0].click()
        time.sleep(1)
finally:
    driver.quit()
print(len(rows))
