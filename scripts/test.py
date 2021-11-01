import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

try:
    browser.get("https://www.ecosia.org")

finally:
    time.sleep(2)
    browser.quit()
