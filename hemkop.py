import time
import datetime
from sympy import product

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv

from selenium.webdriver.firefox.options import Options

time_start = time.time()
options = Options()
options.headless = False

driver = webdriver.Firefox(options=options)
driver.get('https://www.hemkop.se/erbjudanden')

weeknumber = datetime.date.today().isocalendar()[1]
output = open('output/hemkop_promos' + '_w' + str(weeknumber) + '.csv', 'w')
writer = csv.writer(output)

time.sleep(4)
cookie_xpath = '//*[@id="onetrust-reject-all-handler"]'
cookietrust = driver.find_element(By.XPATH, cookie_xpath)
cookietrust.click()

time.sleep(2)

#Skriv i box
storesearch_xpath = '//*[@id="__next"]/div[2]/div[2]/div/div[2]/div/form/div/div/div[2]/input'
storesearch = driver.find_element(By.XPATH, storesearch_xpath)
storesearch.send_keys('Göteborg Vasagatan')

#Klicka på butik
time.sleep(1)
# resultmenu = driver.find_element_by_class_name('store-select-header') #Elementet innan butiklänken
store_element_xpath = '/html/body/div[1]/div[2]/div[2]/div/div[2]/div/form/div/div/div[3]/ul/li'
store_element = driver.find_element(By.XPATH, store_element_xpath)
store_element.click()

time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(3)
grid_xpath = '/html/body/div[1]/div[2]/div[4]/div[1]'

grid = driver.find_element(By.XPATH, grid_xpath)
product_elements = grid.find_elements(By.XPATH, './*')



#relative to infopath
title_xpath = './/*[@data-testid="product-title"][1]'
price_xpath = './/*[contains(@data-testid, "splash")]'
desc_xpath = title_xpath + '/../div'
# compareprice_xpath = './ax-product-puff/div/div[3]/div/ax-product-pricelabel/div/div[1]/span[1]'

for i in product_elements:
    title_elem = i.find_element(By.XPATH, title_xpath)
    price_elem = i.find_element(By.XPATH, price_xpath)
    desc_elem = i.find_element(By.XPATH, desc_xpath)
    
    product_data = [title_elem.text, price_elem.text, desc_elem.text]
    writer.writerow(product_data)
    print(product_data, "\n")

# driver.quit()
time_end = time.time()
print('\nRuntime: ', time_end-time_start)