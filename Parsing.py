import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.wildberries.ru/catalog/11127342/detail.aspx?targetUrl=MI'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/89.0.4389.114 Safari/537.36 '
}
r = requests.get(url, headers=headers)

"""Проверка"""
print(r)
print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
if re.search(r'\bwww.dsquared2.com\b', url):
    name = soup.find('div', {'class': 'infoCta-wrapper'}).find('h1').text
    price = soup.find('div', {'class': 'itemPrice'}).find('span', {'class': 'price'}).find('span',
                                                                                           {'class': 'value'}).get(
        'data-ytos-price')
    print(price, name)
elif re.search(r'\bwww.tsum.ru\b', url):
    name = soup.find('div', {'class': 'item__specifications'}).find('h1').find('a').text
    typo = soup.find('div', {'class': 'item__specifications'}).find('h1').find('span').text
    price = soup.find('div', {'class': 'price price_type_retail ng-star-inserted'}).find('span').text
    print(name, typo, price)
elif re.search(r'\bwww.lamoda.ru\b', url):
    name = soup.find('div', {'class': 'product-title-wrapper'}).find('h1').get('title')
    typo = soup.find('div', {'class': 'product-title-wrapper'}).find('h1').find('span').text
    price = soup.find('div', {'class': 'ii-product-buy'}).find('div', {'class': 'vue-widget'}).text
    print(name, typo, price)
elif re.search(r'\bwww.wildberries.ru\b', url):
    name = soup.find('div', {'class': 'brand-and-name j-product-title'}).find('span', {'class': 'brand'}).text
    typo = soup.find('div', {'class': 'brand-and-name j-product-title'}).find('span', {'class': 'name'}).text
    price = soup.find('div', {'class': 'final-price-block'}).find('span').text
    print(name, typo, price)
elif re.search(r'\bwww.gloria-jeans.ru\b', url):
    name = soup.find('div', {'class': 'basic-info js-block-for-shield'}).find('h1').text
    price = soup.find('div', {'class': 'wrapper-price js-base-price'}).text
    print(name, price)
'''elif re.search(r'\bostin.com\b', url):
    name = soup.find('html', {'class': 'popmechanic-desktop popmechanic-loaded popmechanic-landscape'}).text
    print(name)
    price = soup.find('div', {'class': 'o-product-price__container'}).text'''


