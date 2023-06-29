from bs4 import BeautifulSoup

import requests

website = requests.get('https://www.honda.com.br/motos/modelos').text


soup = BeautifulSoup(website, 'html.parser')

items = soup.findAll('li', class_='item')

for item in items:
    name = item.find('div', class_ = 'title').text.replace("\n", "").replace(" ","")
    price = item.find('span', class_ = 'price').text.replace(" ", "")
    print(f"Model: {name:35} Price: {price}")
