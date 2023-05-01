from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import psycopg2 as psyc
from wget import download
import os
import shutil

images = 'D:\ss\images'
shutil.rmtree(images)
os.makedirs(images)
s = Service('C:\data\hrome\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.ozon.ru/category/telefony-i-smart-chasy-15501/')
time.sleep(3)
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
products = soup.find_all(attrs={"class": "km1 k1m"})
with psyc.connect(host='localhost', dbname='DBNGUYEN', user='postgres', password='15012001') as conn:
    with conn.cursor() as cursor:
        cursor.execute("delete from phone")
        for i, product in enumerate(products):

            img_tag = product.find(attrs={"class": "jy9"}).find("img")
            img_url = img_tag['src']

            filename = f"{i+1}.jpg"
            download(img_url, f"images/{filename}")
            prices = product.find(attrs={"class": "aa2-a0"}).text
            name = product.find(attrs={"class": "tile-hover-target yj4 jy5"}).text
            params = {"name": name}

            cursor.execute(f"""insert into phone( name,prices, file) 
                                values (%(name)s, '{prices}', '{i+1}.jpg');""",params)
        conn.commit()