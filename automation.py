from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import re
import requests
from bs4 import BeautifulSoup
product = input('what do you want to search for?: ').capitalize()

maximum_price = input('what is your maximum price range: ')


chrome_options = Options()

chrome_options.add_experimental_option("detach", True)

chrome_browser = webdriver.Chrome(options=chrome_options)


chrome_browser.get('https://www.jumia.com.ng/')

search_bar = chrome_browser.find_element(By.ID, 'fi-q')
search_bar.send_keys(f'{product}')


search_bar_button = chrome_browser.find_element(
    By.CSS_SELECTOR, '#search > .btn')
search_bar_button.click()

price_min_range = chrome_browser.find_element(By.NAME, 'min')
price_min_range.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
price_min_range.send_keys('10000')

price_max_range = chrome_browser.find_element(By.NAME, 'max')
price_max_range.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
price_max_range.send_keys(f'{maximum_price}')

time.sleep(1)
up_button = chrome_browser.find_element(
    By.XPATH, '//*[@id="jm"]/main/div[3]/a')
ActionChains(chrome_browser).context_click(up_button).perform()

time.sleep(2)
apply_button = chrome_browser.find_element(
    By.XPATH, '//*[@id="jm"]/main/div[2]/div[2]/div/section/header/button')
chrome_browser.execute_script('arguments[0].click()', apply_button)

time.sleep(6)
items_found = {}
res = requests.get(
    f'https://www.jumia.com.ng/catalog/?q={product}&price=10000-{maximum_price}#catalog-listing')
soup = BeautifulSoup(res.text.encode(
    'utf-8').decode('ascii', 'ignore'), 'html.parser')

div = soup.find(class_="-paxs row _no-g _4cl-3cm-shs")

items = div.find_all(text=re.compile(f'{product}'))
for item in items:
    parent = item.parent
    next_parent = parent.parent
    price = next_parent.find(class_='prc').string
    items_found[item] = {'price': int(price.replace(',', ''))}

sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])

for item in sorted_items:
    print(item[0])
    print(f"{item[1]['price']}")
    print('-------------------------------------')
