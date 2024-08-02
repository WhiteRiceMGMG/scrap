from bs4 import BeautifulSoup
import requests

"""
res = requests.get('https://www.orangepage.net/recipes')
soup = BeautifulSoup(res.text,'html.parser')

tag1 = soup.title
text1 = tag1.string
#print(text1)

#find_allですべての要素取得
tag2 = soup.find_all('p')
text2_list = [x.string for x in tag2]
#print(text2_list)
"""
res2 = requests.get('https://www.orangepage.net/recipes/search/3')
soup2 = BeautifulSoup(res2.text,'html.parser')

tag3 = soup2.find_all('p',class_='tit')
text3_list = [x.string for x in tag3]
#print(text3_list)

#主要な野菜も取得
tag4 = soup2.find_all('p',class_='ingredients')
text4_list = [x.string for x in tag4]
#print('text4_list')


recipe = soup2.find('div', id='recipe_list',class_='recipesList')
tag5 = recipe.find_all('h2',class_='tit')
text5_list = [x.string for x in tag5]
print(text5_list)

#レシピの詳細
recipe_detail = soup2.find('div', id='recipe_list',class_='recipesList')
url = recipe_detail.find_all('a')
url_list = [x['href'] for x in url]
print(url_list) 


