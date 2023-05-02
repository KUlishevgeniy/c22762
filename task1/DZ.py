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

with psyc.connect(host='localhost', dbname='mydb', user='postgres', password='12345678') as conn:
    with conn.cursor() as cursor:
        for i, product in enumerate(prodall):



            description = product.find(attrs={"class": "Raw-slyvem-0 DetailCardVacation__DescriptionLarge-sc-17wjakb-11 eFsMWr emOKPv"}).text

            params = {"description": description}
            cursor.execute(f"""insert into images(  description) 
                                values (%(description)s);""",params)

        conn.commit()

