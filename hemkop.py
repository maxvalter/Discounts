from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

time_start = time.time()

options = webdriver.ChromeOptions()
# options.add_argument('--headless') 
options.add_argument('start-maximized') 
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')

PATH ="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome('drivers/chromedriver-2')

driver.get('https://www.hemkop.se/erbjudanden')

time.sleep(4)
cookietrust = driver.find_element_by_id('onetrust-reject-all-handler')
cookietrust.click()

storeselect = driver.find_element_by_class_name('md-select-value')
storeselect.click()

time.sleep(2)

storesearch = driver.find_element_by_xpath('//*[@id="select_container_13"]/md-select-menu/md-content/md-select-header/form/input')
storesearch.send_keys('Linnégatan')

time.sleep(1)
resultmenu = driver.find_element_by_class_name('store-select-header') #Elementet innan butiklänken
store_element = resultmenu.find_element_by_xpath('./following-sibling::md-option')
store_element.click()

time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")



time.sleep(3)
product_grid = driver.find_element_by_xpath('//*[@id="selenium--main-content-wrapper"]/div/ui-view/div/div[2]/div/div/ax-promotion/div/div[2]/div[2]/ax-productdisplay/div/div')
product_elements = product_grid.find_elements_by_xpath('./*')

info_class_name = 'product-puff-body'

#Xpaths relative to product
info_xpath = './ax-product-puff/div/div[3]'
title_xpath = './ax-product-puff/div/div[3]/div/div[2]/a'
price_xpath = './ax-product-puff/div/div[1]/ax-promotion-label/div/div/div'
compareprice_xpath = './ax-product-puff/div/div[3]/div/ax-product-pricelabel/div/div[1]/span[1]'

#Xpaths relative to price element
unit_xpath = './div'

for i in product_elements:
    title = i.find_element_by_xpath(title_xpath)
    price = i.find_element_by_xpath(price_xpath)

    unit = price.find_element_by_xpath(unit_xpath)
    
    compareprice = i.find_element_by_xpath(compareprice_xpath)

    print(title.text, price.text, compareprice.text, "\n")

time_end = time.time()
print('\nRuntime: ', time_end-time_start)