import requests
from bs4 import BeautifulSoup
import mysql.connector as mysql

class scraping():
    title=None
    price=None
    headers =  {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

    def get_details(self, url, website):
        page = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        if website == 'Amazon':
            self.title = soup.find('span', id='productTitle')
            self.price = soup.find('span', id='priceblock_ourprice')
            # try:
            #     price = price.text
            # except:
        elif website == 'Flipkart':
            self.title = soup.find('span', class_='B_NuCI')
            self.price = soup.find('div', class_='_30jeq3 _16Jk6d')
        elif website == 'Shopclues':
            self.title = soup.find('h1', itemprop='name')
            self.price = soup.find('span', class_='f_price')

        self.title = self.title.text.strip()
        self.price = self.price.text
        return self.title, self.price
