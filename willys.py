from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

time_start = time.time()

options = webdriver.ChromeOptions()
# options.add_argument('--headless') 
# options.add_argument('start-maximized') 
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')

PATH ="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome('drivers/chromedriver-2')

driver.get("https://www.willys.se/erbjudanden/butik")
#print(driver.title)

time.sleep(5)


cookietrust = driver.find_element_by_id("onetrust-reject-all-handler")
cookietrust.click()

searchstores = driver.find_element_by_xpath('//*[@id="__next"]/div/div[3]/main/section/div[2]/div[2]/div[1]/div[2]/div/div/input')
searchstores.send_keys('Hvitfeldtsplatsen')

time.sleep(5)

#store = driver.find_element_by_xpath('//*[@id="__next"]/div/div[3]/main/section/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/ul/li/div/div[1]')
store = driver.find_element_by_xpath('//*[@id="__next"]/div/div[3]/main/section/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/ul/ul')
store.click()

time.sleep(5)

#showmore = driver.find_element_by_xpath('//*[@id="__next"]/div/div[3]/main/section/div[2]/div[2]/div[2]/div/div/div[4]/div/button')
#showmore.click()

# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

time.sleep(2)

product_xpath = '//*[@id="__next"]/div/div[3]/main/section/div[2]/div[2]/div[2]/div/div/div[3]'

titleclass = 'Product_product-name__1IyPc'
price_class = 'PriceLabel_product-price-text__3xFzK'

product_grid = driver.find_element_by_xpath(product_xpath)
product_elements = product_grid.find_elements_by_xpath('.//*')

for i in product_elements: #Visar upprepat handskalade räkor
    child = i.find_element_by_xpath('//div[contains(@class,"Product_product-name")]')
    print(child.text)


time.sleep(5)
driver.quit()

time_end = time.time()
print('\nRuntime: ', time_end-time_start)
