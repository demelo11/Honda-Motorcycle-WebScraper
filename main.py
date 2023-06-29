
from bs4 import BeautifulSoup
import csv
import requests
import time

def scrapper():
    website = requests.get('https://www.honda.com.br/motos/modelos').text
    soup = BeautifulSoup(website, 'html.parser')
    items = soup.findAll('li', class_='item')

    filename = "output.csv"
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Model", "Price"])  # Write headers

        for item in items:
            name = item.find('div', class_='title').text.replace("\n", "").replace(" ", "")
            price = item.find('span', class_='price').text.replace(" ", "")
            print(f"Model: {name:35} Price: {price}")
            writer.writerow([name, price])

        print(f"File updated.")

if __name__ == '__main__':
   #run every 20 hours
    while True:
        scrapper()
        time.sleep(600*60*2)