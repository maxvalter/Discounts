import time
time_start = time.time()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

import csv
import datetime



options = Options()
options.headless = True

driver = webdriver.Firefox(options=options, executable_path='drivers/geckodriver')
# driver_path = '/usr/bin/safaridriver'

driver.get("https://www.willys.se/erbjudanden/butik")
#print(driver.title)

weeknumber = datetime.date.today().isocalendar()[1]
output = open('output/willys_promos' + '_w' + str(weeknumber) + '.csv', 'w')
writer = csv.writer(output)

time.sleep(3)

cookietrust = driver.find_element_by_id("onetrust-reject-all-handler")
cookietrust.click()

searchstores = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/main/section/div[2]/div[2]/div/div/div/input')
searchstores.send_keys('Johanneberg')

time.sleep(1)

#store = driver.find_element_by_xpath('//*[@id="__next"]/div/div[3]/main/section/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/ul/li/div/div[1]')
store = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/main/section/div[2]/div[2]/div/div/div[2]/div/ul')
store.click()

time.sleep(2)

showmore = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/main/section/div[2]/div[3]/div/div/div/div[4]/div/button')
showmore.click()

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

time.sleep(4)

grid_xpath = '/html/body/div[1]/div/div[3]/main/section/div[2]/div[3]/div/div/div/div[3]'


#Relative to grid_xpath
product_xpath = './*'  

#Relative to product_xpath
title_xpath = './div[2]/div[1]' 
price_children_xpath = './div[1]/div[2]/*'
brand_xpath = './div[2]/div[2]/span'
desc_xpath = './div[2]/div[2]'


#Relative to price_xpath?
kronor_xpath = './div/div/span'
öre_xpath = './div/div/div/span[1]'
unit_xpath = './div/div/div/span[2]'
multiples_xpath = './div[1]'


product_grid = driver.find_element_by_xpath(grid_xpath)
product_elements = product_grid.find_elements_by_xpath(product_xpath)

for i in range(len(product_elements)-1):
    element = product_elements[i+1] #Skips first, not a product

    title_element = element.find_element_by_xpath(title_xpath)

    desc_element = element.find_element_by_xpath(desc_xpath)


    price_elements = element.find_elements_by_xpath(price_children_xpath)
    price_info = ""
    for child in price_elements:
        price_info = price_info + child.text + ' '


    # kronor_element = price_element.find_element_by_xpath(kronor_xpath)
    # öre_element = price_element.find_element_by_xpath(öre_xpath)
    # unit_element = price_element.find_element_by_xpath(unit_xpath)

    product_data = [title_element.text, price_info.replace('\n', ' '), desc_element.text.replace('\n', ' ')]
    writer.writerow(product_data)

    print('\n' + title_element.text + ": " + repr(price_info.replace('\n', ' ')) + ' ' 
     + repr(desc_element.text))

# element = product_elements[1]
# title_element = element.find_element_by_xpath(title_xpath)
# price_element = element.find_element_by_xpath(price_xpath)
# kronor_element = price_element.find_element_by_xpath(kronor_xpath)
# öre_element = price_element.find_element_by_xpath(öre_xpath)

# print(title_element.text + ": " + kronor_element.text + ',' + öre_element.text)

driver.quit()

time_end = time.time()
print('\nRuntime: ', time_end-time_start)