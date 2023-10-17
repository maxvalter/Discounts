import time
import datetime
from sympy import product
time_start = time.time()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = False

driver = webdriver.Firefox(options=options, executable_path='drivers/geckodriver')
driver.get('https://www.hemkop.se/erbjudanden')

weeknumber = datetime.date.today().isocalendar()[1]
output = open('output/hemkop_promos' + '_w' + str(weeknumber) + '.csv', 'w')
writer = csv.writer(output)

time.sleep(4)
cookietrust = driver.find_element_by_id('onetrust-reject-all-handler')
cookietrust.click()

#------
#Välj butik

#Klicka på box
time.sleep(2)
storeselect = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[4]/div[3]/form/div[2]')
storeselect.click()

time.sleep(2)

#Skriv i box
storesearch = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[4]/div[3]/form/div[2]/div/input')
storesearch.send_keys('Göteborg Vasagatan')

#Klicka på butik
time.sleep(1)
# resultmenu = driver.find_element_by_class_name('store-select-header') #Elementet innan butiklänken
store_element = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[4]/div[3]/form/div[2]/div/div[2]/ul/li[1]')
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
grid_xpath = '/html/body/div[1]/div[1]/div[6]/div[1]'

grid = driver.find_element_by_xpath(grid_xpath)
product_elements = grid.find_elements_by_xpath('./*')


print(len(product_elements))

#Xpaths relative to product
info_xpath = './div/div'
# title_xpath = './div/div/div[4]/div[2]/div/div'

#relative to infopath
title_xpath = './div[4]/div[2]/div/div'
price_xpath = './div[5]'
desc_xpath = './div[4]/div[3]/p'
# compareprice_xpath = './ax-product-puff/div/div[3]/div/ax-product-pricelabel/div/div[1]/span[1]'

for i in product_elements:
    info_elem = i.find_element_by_xpath(info_xpath)
    title_elem = info_elem.find_element_by_xpath(title_xpath)
    price_elem = info_elem.find_element_by_xpath(price_xpath)
    desc_elem = info_elem.find_element_by_xpath(desc_xpath)
    
    product_data = [title_elem.text, price_elem.text, desc_elem.text]
    writer.writerow(product_data)
    print(product_data, "\n")

# driver.quit()
time_end = time.time()
print('\nRuntime: ', time_end-time_start)