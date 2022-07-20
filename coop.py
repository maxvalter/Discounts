from dataclasses import dataclass
import time
import datetime
time_start = time.time()

import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

def fetch_info_from_elements(elements):

    #Xpaths relative to element
    desc_elem_xpath = ".//p[contains(@class, 'ItemTeaser-description')]"
    name_elem_xpath = ".//h3[contains(@class, 'ItemTeaser-heading')]"

    price_splash_xpath = ".//p[contains(@class, 'Splash')]"
    splash_children_xpath = ".//span[contains(@class, 'Splash-content ')]/*"
    
    #relative to splash 
    largevalue_elem_xpath = ".//span[contains(@class, 'Splash-priceLarge')]"
    smallvalue_elem_xpath = "./span/span[3]/span[2]"

    names = []
    prices = []
    brands = []



    for elem in elements:
        name_elem = elem.find_element(by=By.XPATH, value=name_elem_xpath)
        desc_elem = elem.find_element(by=By.XPATH, value=desc_elem_xpath)
        

        splash_children = elem.find_elements(by=By.XPATH, value=splash_children_xpath)
        price_info = ""
        
        for child in splash_children:
            if len(child.text) >= 1:
                price_info = price_info + child.text + ' '
        
        product_data = [name_elem.text, price_info, desc_elem.text]
        writer.writerow(product_data)

        print(name_elem.text + ', ' + desc_elem.text)
        print('\n' + price_info)


#Init
options = Options()
options.headless = False

driver = webdriver.Firefox(options=options, executable_path='drivers/geckodriver')
driver.get('https://www.coop.se/butiker-erbjudanden/coop/coop-landala/')


weeknumber = datetime.date.today().isocalendar()[1]
output = open('output/coop_promos' + '_w' + str(weeknumber) + '.csv', 'w')
writer = csv.writer(output)

#Reject cookies
reject_cookies_xpath = '//*[@id="cmpwelcomebtnno"]/a'
reject_cookies = driver.find_element(by=By.XPATH, value=reject_cookies_xpath)
reject_cookies.click()


#Find body
body_xpath = '/html/body/main/div[2]/div/div[1]/div/div/div[6]'
body_element = driver.find_element(by=By.XPATH, value=body_xpath)

#Find category-grids
grids_xpath = '/html/body/main/div[2]/div/div[1]/div/div/div[6]/*'
grids = driver.find_elements(by=By.XPATH, value=grids_xpath)
grids.pop(0)

print("This week has " + str(len(grids)) + " categories")

#Click on all "show more" buttons (Xpath relative to body)

showmore_xpath = ".//button[contains(text(),'Visa fler')]"
showmore_elements = body_element.find_elements(by=By.XPATH, value=showmore_xpath)


for i in showmore_elements:
    i.click()
    time.sleep(1)


#Relative to category-grid
grid_children_xpath = ".//article[contains(@class, 'ItemTeaser')]"

for grid in grids:
    grid_index = 1

    print("\nscanning grid " + str(grid_index) + "...")
    grid_index = grid_index + 1

    grid_elements = grid.find_elements(by=By.XPATH, value=grid_children_xpath)
    print("This grid has " + str(len(grid_elements)) + " elements")

    fetch_info_from_elements(grid_elements)


# #Xpaths for each category-grid, relative to body
# grid1_xpath = './div[1]'
# grid2_xpath = './div[2]' 
# grid3_xpath = './div[3]'
# grid4_xpath = './div[4]' 

# grid_children_xpath = ".//article[contains(@class, 'ItemTeaser')]"

# #Frukt och grönt
# grid2 = body_element.find_element(by=By.XPATH, value=grid2_xpath)
# grid2_elements = grid2.find_elements(by=By.XPATH, value=grid_children_xpath)
# print('\nfrukt och grönt: ' + str(len(grid2_elements)) + ' erbjudanden')
# fetch_info_from_elements(grid2_elements)

# #Kött
# grid3 = body_element.find_element(by=By.XPATH, value=grid3_xpath)
# grid3_elements = grid3.find_elements(by=By.XPATH, value=grid_children_xpath)
# print('\nKött, färdigmat: ' + str(len(grid3_elements)) + ' erbjudanden')
# fetch_info_from_elements(grid3_elements)

# #Mejeri
# grid4 = body_element.find_element(by=By.XPATH, value=grid4_xpath)
# grid4_elements = grid4.find_elements(by=By.XPATH, value=grid_children_xpath)
# print('\nMejeri: ' + str(len(grid4_elements)) + ' erbjudanden')
# fetch_info_from_elements(grid4_elements)

# #Dryck
# grid5 = body_element.find_element(by=By.XPATH, value=grid5_xpath)
# grid5_elements = grid5.find_elements(by=By.XPATH, value=grid_children_xpath)
# print('\nDryck: ' + str(len(grid5_elements)) + ' erbjudanden')
# fetch_info_from_elements(grid5_elements)

# #Övrigt
# grid6 = body_element.find_element(by=By.XPATH, value=grid6_xpath)
# grid6_elements = grid6.find_elements(by=By.XPATH, value=grid_children_xpath)
# print('\nÖvrigt: ' + str(len(grid6_elements)) + ' erbjudanden')
# fetch_info_from_elements(grid6_elements)

driver.quit()

output.close()
time_end = time.time()
print('\nRuntime: ', time_end-time_start)



