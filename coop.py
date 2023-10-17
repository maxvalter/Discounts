from dataclasses import dataclass
import time
import datetime
time_start = time.time()

import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

#Init
options = Options()
options.headless = False


def get_price(article):
    try:
        price_elem = article.find_element(by=By.XPATH, value=price1_xpath)
    except:
        price_elem = article.find_element(by=By.XPATH, value=price2_xpath)
    
    price_text = price_elem.text
    price_text = price_text.replace('\n', ' ')
    return price_text

def get_weight(article):
    try:
        weight_elem = article.find_element(by=By.XPATH, value=weight_xpath)
        return weight_elem.text
    except: 
        print('no_weight')
        return None
        # desc_elem = i.find_element(by=By.XPATH, value=desc_xpath)


def data_from_spoiler(article,spoiler_xpath,grid):
    spoiler_button = article.find_element(by=By.XPATH, value=spoiler_xpath)
    spoiler_button.click()
    time.sleep(0.5)
    spoiled_article = grid.find_element(by=By.XPATH, value=spoiled_children_xpath)
    data = data_from_article(spoiled_article)

    spoiler_button.click()
    return data

def data_from_article(article):
    #Spoiled stängd
    data = [article.find_element(by=By.XPATH, value=title_xpath).text.replace('\n', ' '),
        get_price(article),
        article.find_element(by=By.XPATH, value=desc_xpath).text]

    print(data)
    return data

def data_from_grid(grid):
    data = []
    for article in grid.find_elements(by=By.XPATH, value=grid_children_xpath):
        try:
            data.append(data_from_spoiler(article,spoiler_xpath,grid))
        except:
            data.append(data_from_article(article))
    return data

def write_from_grid(grid):
    data = data_from_grid(grid)
    writer.writerows(data)

driver = webdriver.Firefox(options=options, executable_path='drivers/geckodriver')
driver.get('https://www.coop.se/butiker-erbjudanden/coop/coop-landala/')

weeknumber = datetime.date.today().isocalendar()[1]
output = open('output/coop_promos' + '_w' + str(weeknumber) + '.csv', 'w')

global writer
writer = csv.writer(output)

#Reject cookies
reject_cookies_xpath = '//*[@id="cmpwelcomebtnno"]/a'
reject_cookies = driver.find_element(by=By.XPATH, value=reject_cookies_xpath)
reject_cookies.click()

#---
#Log-in
time.sleep(3)
login_xpath = '/html/body/main/div[2]/div[2]/div[1]/div/div/div[2]/h3/a'
login_element = driver.find_element(by=By.XPATH, value=login_xpath)
login_element.click()

#Fill form
time.sleep(2.5)
email_xpath = '//*[@id="loginEmail"]'
pass_xpath = '//*[@id="loginPassword"]'
email_input = driver.find_element(by=By.XPATH, value=email_xpath)
pass_input = driver.find_element(by=By.XPATH, value=pass_xpath)
email_input.send_keys('hejdetarmax@gmail.com')
pass_input.send_keys('lillolga')

submit_xpath = '/html/body/div/div/div/form/footer/button'
submit_button = driver.find_element(by=By.XPATH, value=submit_xpath)
submit_button.click()

# #Find body
# time.sleep(1)
# body_xpath = '/html/body/main/div[2]/div[2]/div[3]/div/div[2]/div/div'
# body_element = driver.find_element(by=By.XPATH, value=body_xpath)

#Find category-grids
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

student_grid_xpath = '/html/body/main/div[2]/div[2]/div[1]/div/div[3]/div'


print("Searching personal discounts...\n")

s_grid = driver.find_element(by=By.XPATH, value=student_grid_xpath)
s_grid_elems_pop = s_grid.find_elements(by=By.XPATH, value='./div')
s_grid_elems = s_grid_elems_pop[1:]

print("Found", len(s_grid_elems), "items.\n")

s_disc_xpath = './article/div/div[2]/div[2]/div/div/p/span/span[1]'
s_disc_class = 'Splash-content'
s_info_class = 'ItemTeaser-info'
#Relative to info_box
s_title_xpath = './h3'
s_desc_xpath = './div'


writer.writerow(['Personliga:', '', ''])

for i in s_grid_elems:
    s_disc = i.find_element(by=By.CLASS_NAME, value=s_disc_class)
    info_box = i.find_element(by=By.CLASS_NAME, value=s_info_class)
   
    s_title = info_box.find_element(by=By.XPATH, value=s_title_xpath)
    s_desc = info_box.find_element(by=By.XPATH, value=s_desc_xpath)

    product_data = [s_title.text, s_disc.text, s_desc.text]
    writer.writerow(product_data)
    print(product_data, "\n")
    # print(i.text)

writer.writerow(['', '', ''])

#---RESTEN---

other_grids1 = '/html/body/main/div[2]/div[2]/div[3]'
other_grids2 = '/html/body/main/div[2]/div[2]/div[2]'

grids = driver.find_element(by=By.XPATH, value=other_grids2)

#Relative to gridS
grid_xpath = './*'
grids_elems = grids.find_elements(by=By.XPATH, value=grid_xpath)

#Relative to grid
global grid_children_xpath, button_xpath
grid_children_xpath = './div[2]/div/div/div/article'
button_xpath = './div[3]/button'
spoiled_children_xpath = './/div[@class="swiper-wrapper"]//article'

#Relative to article
global price1_xpath, price2_xpath, title_xpath, weight_xpath, desc_xpath, spoiler_xpath, spoiled_elements
price1_xpath = './div/div[1]/div[3]/div/div/p/span'
price2_xpath = './div/div[1]/div[2]/div/div/p/span'
title_xpath = './div/div[2]/div[1]'
weight_xpath =  './div/div[2]/div[1]/div/div'
desc_xpath = './div/div[2]/div[2]/div[3]'
spoiler_xpath = './/button[contains(text(), "Visa")]'
spoiled_elements_xpath = '../div[@class="Grid-cell u-sizeFull u-paddingAz"]/div/div/div/div/div/div/div/div/article'

for grid in grids_elems:
    
    product_data = data_from_grid(grid)

    writer.writerows(product_data)
    print(product_data, "\n")

driver.quit()

output.close()
time_end = time.time()
print('\nRuntime: ', time_end-time_start)



