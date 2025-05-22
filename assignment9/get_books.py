import pandas as pd
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
driver.get(url)

time.sleep(5)

results_elements = driver.find_elements(By.CSS_SELECTOR, "li.cp-search-result-item")
print(f"Found {len(results_elements)} results.")

results = []

for result in results_elements:
    try:
        # Extract title
        title_element = result.find_element(By.CSS_SELECTOR, "span.title-content")
        title = title_element.text.strip()
    except:
        title = "N/A"

    try:
        # Extract all authors (may be multiple)
        author_container = result.find_element(By.CSS_SELECTOR, "span.cp-author-link")
        author_elements = author_container.find_elements(By.CSS_SELECTOR, "a.author-link")
        authors = "; ".join([a.text.strip() for a in author_elements])
    except:
        authors = "N/A"

    try:
        # Extract format and year
        format_year_element = result.find_element(By.CSS_SELECTOR, "span.display-info-primary")
        format_year_raw = format_year_element.text.strip()
        format_year = format_year_raw.split("|")[0].strip()  # removed language
    except:
        format_year = "N/A"

    book_data = {
        "Title": title,
        "Author": authors,
        "Format-Year": format_year
    }

    results.append(book_data)

driver.quit()

df = pd.DataFrame(results)
print(df)

df.to_csv("books.csv", index=False)
with open("books.json", "w") as f:
    json.dump(results, f, indent=2)
