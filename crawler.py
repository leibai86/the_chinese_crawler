# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup



def book_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://www.txt80.com/dushi/index_' + str(page) + '.html'
        source_code = requests.get(url)
        #source_code.encoding = 'gb18030'
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,'lxml')  # all the souce code from the object. like all the link/ title
        for link in soup.findAll('a', {'target': '_blank'}):  # 'a' is anker in HTML. loop all the info we get target is blank.
            href ="http://www.txt80.com" + link.get('href')
            title = link.string
            n = 'www.txt80.com/recommend100.html'
            if n in href:
                continue
            print(title)
            print(href)
            get_single_data(href)
        page += 1

def get_single_data(item_url):
    source_code = requests.get(item_url)
    # source_code.encoding = 'gb18030'
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    for item_name in soup.findAll('div', {'class': 'cont'}):
        print(item_name.string)

    '''for link in soup.findAll('a'):
        href = "http://www.txt80.com" + link.get('href')
        print(href)'''


book_spider(2)

