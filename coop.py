from dataclasses import dataclass
import time
import datetime
time_start = time.time()

import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def get_shadow_root(element):
    return driver.execute_script('return arguments[0].shadowRoot', element)

def get_price(article):
    price1_xpath = './div/div[1]/div[3]/div/div/p/span'
    price2_xpath = './div/div[1]/div[2]/div/div/p/span'
    price_class = 'ProductTeaser-splash'
    try:
        price_elem = article.find_element(by=By.CLASS, value=price_class)
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
    price_xpath = './article/div/div[1]/div[3]/div/div/div[1]/div'
    title = article.find_element(by=By.XPATH, value=title_xpath).text.replace('\n', ' ')
    price = article.find_element(by=By.XPATH, value=price_xpath).text.replace('\n', ' ')
    desc =  article.find_element(by=By.XPATH, value=desc_xpath).text.replace('\n', ' ')
    desc = desc.replace(title, '')
    data = [title,
        price,
       desc]

    print(data)
    return data

def data_from_grid(grid):
    grid_childrens_xpath = './div[1]/div[2]/div/div/div'
    data = []
    grid_childrens = grid.find_elements(by=By.XPATH, value=grid_childrens_xpath)
    for article in grid_childrens:
            data.append(data_from_article(article))
    return data

def write_from_grid(grid):
    data = data_from_grid(grid)
    writer.writerows(data)

options = Options()
options.add_argument("--headless")  # Explicitly add headless mode
options.add_argument("--disable-gpu")  # Sometimes needed for headless mode


driver = webdriver.Firefox(options=options)
driver.get('https://www.coop.se/butiker-erbjudanden/coop/coop-mariagatan/')

timeout = 10
wait = WebDriverWait(driver, timeout)

# Locate the shadow host element
shadow_host = driver.find_element(By.CSS_SELECTOR, '#cmpwrapper')

# Access the shadow root using JavaScript
shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)

#Reject cookies
# Wait for the "Avvisa alla" button to be visible and click it
wait.until(lambda driver: shadow_root.find_element(By.CSS_SELECTOR, '.cmpboxbtnno')).click()

# Wait until the element is no longer visible
wait.until(EC.invisibility_of_element_located((By.ID, 'usercentrics-root')))

#---

# #Find body
# time.sleep(1)
# body_xpath = '/html/body/main/div[2]/div[2]/div[3]/div/div[2]/div/div'
# body_element = driver.find_element(by=By.XPATH, value=body_xpath)

#Find category-grids

##STUDENT DISCOUNTS
# student_grid_xpath = '/html/body/main/div[2]/div/div[3]/div[2]/div[2]/div/div'


# print("Searching personal discounts...\n")

# s_grid = driver.find_element(by=By.XPATH, value=student_grid_xpath)
# s_grid_elems = s_grid.find_elements(by=By.XPATH, value='./div')
# #First element is a header
# s_grid_elems = s_grid_elems[1:]

# print("Found", len(s_grid_elems), "items.\n")

# s_disc_info_xpath = './div/article/div'
# s_disc_class = 'ItemTeaser-splash'
# s_info_class = 'ItemTeaser-info'
# #Relative to info_box
# s_title_xpath = './h3'
# s_desc_xpath = './div'


# writer.writerow(['Personliga:', '', ''])

# for i in s_grid_elems:
#     s_disc = i.find_element(by=By.CLASS_NAME, value=s_disc_class)
#     info_box = i.find_element(by=By.CLASS_NAME, value=s_info_class)
   
#     s_title = info_box.find_element(by=By.XPATH, value=s_title_xpath)
#     s_desc = info_box.find_element(by=By.XPATH, value=s_desc_xpath)

#     product_data = [s_title.text, s_disc.text, s_desc.text]
#     writer.writerow(product_data)
#     print(product_data, "\n")
#     # print(i.text)

# writer.writerow(['', '', ''])

#---RESTEN---

#Relative to grid
global button_xpath
button_xpath = './div[3]/button'
spoiled_children_xpath = './/div[@class="swiper-wrapper"]//article'

#Relative to article
title_xpath = './div/div[2]/div[1]'
weight_xpath =  './div/div[2]/div[1]/div/div'
desc_xpath = './div/div[2]'
spoiler_xpath = './/button[contains(text(), "Visa")]'
spoiled_elements_xpath = '../div[@class="Grid-cell u-sizeFull u-paddingAz"]/div/div/div/div/div/div/div/div/article'

# WRITING Inits
weeknumber = datetime.date.today().isocalendar()[1]
output = open('output/coop_promos' + '_w' + str(weeknumber) + '.csv', 'w')
writer = csv.writer(output)


other_grids = '/html/body/main/div[2]/div/div[3]/div'
grids = driver.find_elements(by=By.XPATH, value=other_grids)

#Paths

for grid in grids:

    #Click 'show more' if it exists
    try:
        show_more_xpath = './div[3]/button'
        show_more = grid.find_element(by=By.XPATH, value=show_more_xpath)
        show_more.click()
    except:
        pass    

    #Find grid elements, generalized css selector
    children_css_selector = 'div.Section:nth-child(3) > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div'
    grid_childrens = grid.find_elements(by=By.CSS_SELECTOR, value=children_css_selector)

    #Paths relative to grid element
    title_xpath = './article/div/div[2]/div[1]/h3'
    price_xpath = './article/div/div[1]/div[3]/div/div/div[1]/div'

    #Filter out gridchildrens without text
    grid_childrens = [i for i in grid_childrens if i.text != '']

    for article in grid_childrens:
        title = article.find_element(by=By.XPATH, value=title_xpath).text.replace('\n', ' ')
        price = article.find_element(by=By.XPATH, value=price_xpath).text.replace('\n', ' ')
        data = [title, price]
        print(data[0], data[1])
        writer.writerow(data)


driver.quit()

output.close()
time_end = time.time()
print('\nRuntime: ', time_end-time_start)



