import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/DualSense-Wireless-Controller-PlayStation-5/dp/B08FC6C75Y/ref=sr_1_1?dchild=1&fst=as%3Aoff&pf_rd_i=16225016011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=03b28c2c-71e9-4947-aa06-f8b5dc8bf880&pf_rd_r=EBPY2Q9M60T8GE8C83V0&pf_rd_s=merchandised-search-3&pf_rd_t=101&qid=1489016289&rnid=16225016011&s=videogames-intl-ship&sr=1-1'
headers =  {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find('span', class_='a-size-large product-title-word-break')
price = soup.find('span', class_='a-size-medium a-color-price priceBlockBuyingPriceString')

print(title.text)
print(price.text)

