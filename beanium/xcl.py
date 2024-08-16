import requests
from bs4 import BeautifulSoup
import openpyxl

url = requests.get('https://www.kikkoman.com/jp/news/2024/')
soup = BeautifulSoup(url.content.decode("utf-8", "ignore"), 'html.parser')
wrap = soup.find('div', class_='cmn-news')
date = wrap.find_all('div', class_="cmn-news_date")
date_list = [x.get_text() for x in date]
print(date_list)
title = wrap.find_all('div', class_="cmn-news_title")
