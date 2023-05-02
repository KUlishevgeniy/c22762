from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
s = Service('C:\data\hrome\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.ozon.ru/category/telefony-i-smart-chasy-15501/')
time.sleep(15)
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
products = soup.find_all('span', class_='em4 me4 em5 em7 tsBodyL yj4 jy5')
print(products[0].text)
print(products[1].text)
