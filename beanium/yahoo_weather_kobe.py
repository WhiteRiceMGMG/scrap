from bs4 import BeautifulSoup
import requests

url = requests.get('https://weather.yahoo.co.jp/weather/jp/28/6310.html')
soup = BeautifulSoup(url.text,'html.parser')

wrap = soup.find('div', class_="forecastCity")
date = wrap.find('span').string
#weather = wrap.get('alt')
weather_p = wrap.find('p',class_='pict')
weather = weather_p.img.get('alt')
print(date + weather)