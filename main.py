from bs4 import BeautifulSoup

import requests

website = requests.get('https://www.honda.com.br/motos/modelos').text


soup = BeautifulSoup(website, 'html.parser')


name = soup.find('div', class_ = 'title').text
print(name)
price = soup.find('span', class_ = 'price').text
print(price)
