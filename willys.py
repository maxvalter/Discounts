from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

time_start = time.time()

options = webdriver.FirefoxOptions()
# # options.add_argument('--headless') 
# options.add_argument('start-maximized') 
# options.add_argument('disable-infobars')
# options.add_argument('--disable-extensions')

driver_path = '/Users/maxadolfsson/Webb/Webscrape/PyScrape/drivers/geckodriver'
# driver_path = '/usr/bin/safaridriver'

# driver = webdriver.Chrome('drivers/chromedriver-2')
driver = webdriver.Firefox(executable_path=driver_path)

driver.get("https://www.willys.se/erbjudanden/butik")
#print(driver.title)

time.sleep(3)

cookietrust = driver.find_element_by_id("onetrust-reject-all-handler")
cookietrust.click()

searchstores = driver.find_element_by_xpath('//*[@id="__next"]/div/div[3]/main/section/div[2]/div[2]/div[1]/div[2]/div/div/input')
searchstores.send_keys('Hvitfeldtsplatsen')

time.sleep(3)

#store = driver.find_element_by_xpath('//*[@id="__next"]/div/div[3]/main/section/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/ul/li/div/div[1]')
store = driver.find_element_by_xpath('//*[@id="__next"]/div/div[3]/main/section/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/ul/ul')
store.click()

time.sleep(5)

showmore = driver.find_element_by_xpath('//*[@id="__next"]/div/div[3]/main/section/div[2]/div[2]/div[2]/div/div/div[4]/div/button')
showmore.click()

# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

time.sleep(4)

grid_xpath = '//*[@id="__next"]/div/div[3]/main/section/div[2]/div[2]/div[2]/div/div/div[3]'
product_xpath = './*'  #Relative to grid_xpath

title_xpath = './div[2]/div[1]' #Relative to product_xpath
price_xpath = './div[1]/div[2]/div/div' #Relative to product_xpath

kronor_xpath = './span'
öre_xpath = './div/span[1]'
unit_xpath = './div/span[2]'

product_grid = driver.find_element_by_xpath(grid_xpath)
product_elements = product_grid.find_elements_by_xpath(product_xpath)
title_elements = []# product_grid.find_elements_by_xpath(title_xpath)


for i in range(len(product_elements)-1):
    element = product_elements[i+1] #Skips first, not a product
    title_element = element.find_element_by_xpath(title_xpath)
    price_element = element.find_element_by_xpath(price_xpath)
    kronor_element = price_element.find_element_by_xpath(kronor_xpath)
    öre_element = price_element.find_element_by_xpath(öre_xpath)
    unit_element = price_element.find_element_by_xpath(unit_xpath)

    print(title_element.text + ": " + kronor_element.text + ',' + öre_element.text + ' ' + unit_element.text)

# element = product_elements[1]
# title_element = element.find_element_by_xpath(title_xpath)
# price_element = element.find_element_by_xpath(price_xpath)
# kronor_element = price_element.find_element_by_xpath(kronor_xpath)
# öre_element = price_element.find_element_by_xpath(öre_xpath)

# print(title_element.text + ": " + kronor_element.text + ',' + öre_element.text)

time.sleep(5)
driver.quit()

time_end = time.time()
print('\nRuntime: ', time_end-time_start)