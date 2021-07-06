from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH ="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.willys.se/anvandare/inloggning")
#print(driver.title)

time.sleep(2)

cookietrust = driver.find_element_by_id("onetrust-reject-all-handler")
cookietrust.click()

user = driver.find_element_by_id("selenium--login-ssn-input")
user.send_keys("200004225496")

password = driver.find_element_by_id("input_8")
password.send_keys("Lillolga")

#time.sleep(2)

submit = driver.find_element_by_xpath("//button[@class='ax-btn-primary md-button md-ink-ripple']")
submit.click()

driver.get("https://www.willys.se/erbjudanden/butik")
time.sleep(4)
products = driver.find_elements_by_class_name("Product_product-name__1IyPc")
print("jello")
#print(products)


for product in products:
    print(product.text)


#driver.quit()
