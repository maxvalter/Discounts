from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time

url = "https://willys.se"

driver = webdriver.Chrome()

driver.get(url)


time.sleep(7)

cookies = driver.find_element_by_id("onetrust-accept-btn-handler")
cookies.click()

soup = BeautifulSoup(driver.page_source, 'html.parser')

product = soup.find("div", class_="ax-product-info")
print(product)