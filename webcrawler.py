import requests
from bs4 import BeautifulSoup

# def perfume_spider():
#     url = "http://www.epocacosmeticos.com.br/perfumes"
#     source_code = requests.get(url)
#     plain_text = source_code.text
#     soup = BeautifulSoup(plain_text)
#     for link in soup.findAll('a',{'class': "productImage"}):
#         href = link.get("href")
#         title = link.get("title")
#         print(href, title)
#
# perfume_spider()
#
#
# def corpo_spider():
#     url = "http://www.epocacosmeticos.com.br/corpo-e-banho"
#     source_code = requests.get(url)
#     plain_text = source_code.text
#     soup = BeautifulSoup(plain_text)
#     for link in soup.findAll('a',{'class': "productImage"}):
#         href = link.get("href")
#         title = link.get("title")
#         print(href, title)
#
# corpo_spider()

def spider():
    url_base = "http://www.epocacosmeticos.com.br/"
    complementos = ["perfumes", "maquiagem", "cabelos", "dermocosmeticos", "tratamentos", "corpo-e-banho"]
    for c in complementos:
        url = url_base + c
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a',{'class': "productImage"}):
            href = link.get("href")
            title = link.get("title")
            print(href, title)

spider()