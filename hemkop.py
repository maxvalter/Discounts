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

time.sleep(2)
storeselect = driver.find_element_by_class_name('md-select-value')
storeselect.click()

time.sleep(2)

storesearch = driver.find_element_by_xpath('/html/body/div[7]/md-select-menu/md-content/md-select-header/form/input')
storesearch.send_keys('Göteborg Vasagatan')

time.sleep(1)
resultmenu = driver.find_element_by_class_name('store-select-header') #Elementet innan butiklänken
store_element = resultmenu.find_element_by_xpath('./following-sibling::md-option')
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
grid_xpath = '/html/body/div[3]/div[6]/div/ui-view/div/div[2]/div/div/ax-promotion/div/div[2]/div[2]/ax-productdisplay/div/div[1]'

grid = driver.find_element_by_xpath(grid_xpath)
product_elements = grid.find_elements_by_xpath('./*')


print(len(product_elements))

#Xpaths relative to product
info_xpath = './ax-product-puff/div/div[3]'
title_xpath = './ax-product-puff/div/div[3]/div/div[2]/a'
price_xpath = './ax-product-puff/div/div[1]/ax-promotion-label/div/div'
desc_xpath = './ax-product-puff/div/div[3]/div/div[3]'
# compareprice_xpath = './ax-product-puff/div/div[3]/div/ax-product-pricelabel/div/div[1]/span[1]'

for i in product_elements:
    title_elem = i.find_element_by_xpath(title_xpath)
    price_elem = i.find_element_by_xpath(price_xpath)
    desc_elem = i.find_element_by_xpath(desc_xpath)
    
    product_data = [title_elem.text, price_elem.text, desc_elem.text]
    writer.writerow(product_data)
    print(title_elem.text, price_elem.text, desc_elem.text, "\n")

driver.quit()
time_end = time.time()
print('\nRuntime: ', time_end-time_start)