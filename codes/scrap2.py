import requests

# url = 'https://twitter.com/'
# screen_name = 'alien_merchant'
# status_id = '674104400013578240'
# url = 'https://twitter.com/' + screen_name + '/status/' + status_id
# # url = 'https://google.com'
# print(url)
# print(requests.get(url).text)


import selenium
from selenium import webdriver
import bs4
driver = webdriver.Firefox()

url = 'https://twitter.com/artingarmsirii/status/1361312811696205827'

bs4.BeautifulSoup
driver.get(url)
import time
time.sleep(3)
# like_button = driver.find_element_by_xpath("//div[text()='Likes']")
like_button = driver.find_element_by_xpath('//*[contains(text(), "Likes")]')
# like_button = like_button.find_element_by_xpath('..')
print(like_button.text)
like_button.click()
