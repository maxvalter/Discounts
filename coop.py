from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

time_start = time.time()

options = webdriver.FirefoxOptions()

driver = webdriver.Firefox(executable_path='drivers/geckodriver')

driver.get('https://www.coop.se/butiker-erbjudanden/coop-butiker/coop-goteborg-andra-langgatan/')

reject_cookies_xpath = '//*[@id="cmpwelcomebtnno"]/a'
reject_cookies = driver.find_element(by=By.XPATH, value=reject_cookies_xpath)
reject_cookies.click()

body_xpath = '/html/body/main/div[2]/div/div[1]/div/div/div[6]'
body_element = driver.find_element(by=By.XPATH, value=body_xpath)

#Xpaths relative to body
showmore_xpath = ".//button[contains(text(),'Visa fler')]"
grid1_xpath = './div[1]'
grid2_xpath = './div[2]' 
grid3_xpath = './div[3]'
grid4_xpath = './div[4]' 
grid5_xpath = './div[5]'
grid6_xpath = './div[6]'

def fetch_info_from_elements(elements):

    price_splash_xpath = ".//p[contains(@class, 'Splash')]"
    name_elem_xpath = ".//h3[contains(@class, 'ItemTeaser-heading')]"

    splash_children_xpath = ".//span[contains(@class, 'Splash-content ')]/*"
    
    #relative to splash
    
    largevalue_elem_xpath = ".//span[contains(@class, 'Splash-priceLarge')]"
    smallvalue_elem_xpath = "./span/span[3]/span[2]"

    

    names = []
    prices = []

    for elem in elements:
        name_elem = elem.find_element(by=By.XPATH, value=name_elem_xpath)

        splash_children = elem.find_elements(by=By.XPATH, value=splash_children_xpath)
        price_info = ""
        for child in splash_children:

            if child.text != " ":
                price_info = price_info + ' ' + child.text
        


        names.append(name_elem.text)
        prices.append(price_info)


        print(name_elem.text + ': ' + price_info)



showmore_elements = body_element.find_elements(by=By.XPATH, value=showmore_xpath)

for i in showmore_elements:
    i.click()
    time.sleep(1)


grid_children_xpath = ".//article[contains(@class, 'ItemTeaser')]"


#Bästa erbjudanden
# grid1 = body_element.find_element(by=By.XPATH, value=grid1_xpath)
# grid1_elements = grid1.find_elements(by=By.XPATH, value=grid_children_xpath)
# print(len(grid1_elements))


#Frukt och grönt
grid2 = body_element.find_element(by=By.XPATH, value=grid2_xpath)
grid2_elements = grid2.find_elements(by=By.XPATH, value=grid_children_xpath)
print('\nfrukt och grönt: ' + str(len(grid2_elements)) + ' erbjudanden')
fetch_info_from_elements(grid2_elements)

grid3 = body_element.find_element(by=By.XPATH, value=grid3_xpath)
grid3_elements = grid3.find_elements(by=By.XPATH, value=grid_children_xpath)
print('\nKött, färdigmat: ' + str(len(grid3_elements)) + ' erbjudanden')
fetch_info_from_elements(grid3_elements)

grid4 = body_element.find_element(by=By.XPATH, value=grid4_xpath)
grid4_elements = grid4.find_elements(by=By.XPATH, value=grid_children_xpath)
print('\nMejeri: ' + str(len(grid4_elements)) + ' erbjudanden')
fetch_info_from_elements(grid4_elements)

grid5 = body_element.find_element(by=By.XPATH, value=grid5_xpath)
grid5_elements = grid5.find_elements(by=By.XPATH, value=grid_children_xpath)
print('\nDryck: ' + str(len(grid5_elements)) + ' erbjudanden')
fetch_info_from_elements(grid5_elements)

grid6 = body_element.find_element(by=By.XPATH, value=grid6_xpath)
grid6_elements = grid6.find_elements(by=By.XPATH, value=grid_children_xpath)
print('\nÖvrigt: ' + str(len(grid6_elements)) + ' erbjudanden')
fetch_info_from_elements(grid6_elements)

driver.quit()
time_end = time.time()
print('\nRuntime: ', time_end-time_start)



