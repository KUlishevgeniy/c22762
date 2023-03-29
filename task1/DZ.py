from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from wget import download
import psycopg2 as psyc

brow = webdriver.Chrome()
url = "https://travel.usnews.com/rankings/worlds-best-vacations/"
brow.get(url)

html = brow.page_source

soup = BeautifulSoup(html, "lxml")

prodall = soup.find_all(attrs={"class": "DetailCardVacation__NoWrapContainer-sc-17wjakb-1 bAXyAM"})

with psyc.connect(host='localhost', dbname='PythonDB', user='postgres', password='qwerty') as conn:
    with conn.cursor() as cursor:
        for i, product in enumerate(all):
            img_tag = product.find(attrs={"class": "Image__Picture-sc-412cjc-0"}).find("img")
            place = product.find(attrs={"class": "Anchor-byh49a-0 dKVMQA"}).text
            image = url + img_tag.attrs.get("src")
            desc = product.find(attrs={"class": "Raw-slyvem-0 DetailCardVacation__DescriptionLarge-sc-17wjakb-11 eFsMWr emOKPv"}).text
            download(url + img_tag.attrs.get("src"), f"images/{i}.jpg")

            cursor.execute(f"""insert into images(link, name, description, file)
                               values ('{image}', '{place}', '{desc}', 'images/{i}.jpg')""")

        conn.commit()