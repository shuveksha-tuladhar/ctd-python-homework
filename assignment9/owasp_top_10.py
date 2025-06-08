import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://owasp.org/www-project-top-ten/"
driver.get(url)

time.sleep(5)

vuln_items = driver.find_elements(By.XPATH, '//*[@id="sec-main"]/ul[2]/li')

results = []

for item in vuln_items:
    try:
        a_tag = item.find_element(By.TAG_NAME, "a")
        title = a_tag.text.strip()
        link = a_tag.get_attribute("href")
    except Exception as e:
        title = "N/A"
        link = "N/A"
    
    results.append({"Title": title, "Link": link})

driver.quit()

print("Extracted OWASP Top 10 Vulnerabilities:")
for r in results:
    print(r)

df = pd.DataFrame(results)
df.to_csv("owasp_top_10.csv", index=False)
