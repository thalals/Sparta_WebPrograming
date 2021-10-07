from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import NoSuchElementException
from pymongo import MongoClient
import requests


client = MongoClient('내AWS아이피', 27017, username="아이디", password="비밀번호")
db = client.dbsparta_plus_week3

driver = webdriver.Chrome('./chromedriver')

url = "http://matstar.sbs.co.kr/location.html"

driver.get(url)
time.sleep(5)

for i in range(10):
    try:
        btn_more = driver.find_element_by_css_selector("#foodstar-front-location-curation-more-self > div > button")
        btn_more.click()
        time.sleep(5)
    except NoSuchElementException:
        break

req = driver.page_source
driver.quit()

soup = BeautifulSoup(req, 'html.parser')

places = soup.select("ul.restaurant_list > div > div > li > div > a")
print(len(places))

for place in places:
    title = place.select_one("strong.box_module_title").text
    address = place.select_one("div.box_module_cont > div > div > div.mil_inner_spot > span.il_text").text
    category = place.select_one("div.box_module_cont > div > div > div.mil_inner_kind > span.il_text").text
    show, episode = place.select_one("div.box_module_cont > div > div > div.mil_inner_tv > span.il_text").text.rsplit(" ", 1)
    print(title, address, category, show, episode)