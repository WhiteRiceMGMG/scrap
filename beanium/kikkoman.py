from bs4 import BeautifulSoup
import requests
import os
import re
import uuid

url = requests.get('https://www.kikkoman.co.jp/homecook/theme/popular/')
soup = BeautifulSoup(url.content.decode("utf-8", "ignore"), 'html.parser')
wrap = soup.find('div', class_='cmn-recipe-card-wrap')
title = wrap.find_all('div', class_="cmn-recipe-card__title")
#find_allの要素はリストで帰ってくるので，要素すべてにget_text()を使う
title_list = [x.get_text() for x in title]
#print(title_list)

imgs = soup.find_all('img',class_='cmn-recipe-card__image__inner')
if not os.path.exists('img-kiko'):
    os.makedirs('img-kiko')
for img in imgs:
    print(img['src'])
    req_img = requests.get(img['src'])
    #img_name = os.path.join("img_kiko", os.path.basename(img_url))
    with open(str('img-kiko/')+str(uuid.uuid4()), 'wb') as file:
        file.write(req_img.content)




