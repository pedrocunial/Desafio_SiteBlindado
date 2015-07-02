import requests
from bs4 import BeautifulSoup

def perfume_spider():
    url = "http://www.epocacosmeticos.com.br/perfumes"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a',{'class': "productImage"}):
        href = link.get("href")
        title = link.get("title")
        print(href, title)

perfume_spider()


