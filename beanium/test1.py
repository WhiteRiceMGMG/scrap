from bs4 import BeautifulSoup
import requests
import os
import uuid

url = requests.get('https://www.kikkoman.co.jp/homecook/theme/popular/')
soup = BeautifulSoup(url.content.decode("utf-8", "ignore"), 'html.parser')


wrap = soup.find('div', class_='cmn-recipe-card-wrap')

title = wrap.find_all('div', class_="cmn-recipe-card__title")
title_list = [x.get_text() for x in title]
print(title_list)

# 画像のパスを取得
imgs = wrap.find_all('div', class_='cmn-recipe-card__image__inner')
for img in imgs:
    # 画像のURLを取得し、完全なURLを形成
    img_tag = img.find('img')
    if img_tag and 'src' in img_tag.attrs:
        img_url = 'https://www.kikkoman.co.jp' + img_tag['src']
        print(img_url)

        # 画像をリクエストで取得
        req_img = requests.get(img_url)

        # img-kikoフォルダが存在しなければ作成
        if not os.path.exists('img-kiko'):
            os.makedirs('img-kiko')

        # ファイル名をUUIDで作成
        img_name = os.path.join('img-kiko', str(uuid.uuid4()) + '.jpg')

        # 画像をファイルに書き込む
        with open(img_name, 'wb') as file:
            file.write(req_img.content)
