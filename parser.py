import requests
from bs4 import BeautifulSoup
import csv
import win32com.client

from  datetime import datetime
from  multiprocessing import Pool

def get_html(url):
    response = requests.get(url) # Response
    return response.text

def get_all_links(html):        # return html code url-page
    soup = BeautifulSoup(html, 'lxml')

    divs = soup.find('div', class_= 'catalog-category').find_all('div', class_= 'thumbnail')
     #print(divs)

    links = []

    for div in divs:
        a = div.find('a', class_= 'ec-price-item-link').get('href')
        link = 'http://www.dns-shop.ru' + a
        links.append(link)

    return links

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    try:
        name = soup.find('h1', class_='page-title price-item-title').text.strip()
    except:
        name = ''

    try:
        price = soup.find('div', class_='price_g').text.strip()
    except:
        price = ''

    data = {'nameProcPrimer': name,
            'priceProcPrimer': price}
    return data


def write_csv(data):
    with open('dns.csv', 'a') as fileProcPrimer:
        writer = csv.writer(fileProcPrimer)

        writer.writerow( (data['nameProcPrimer'],
                          data['priceProcPrimer']))

        print(data['nameProcPrimer'], data['priceProcPrimer'], 'parsed')

def make_all(url):
    html = get_html(url)
    data = get_page_data(html)
    write_csv(data)

def main():
    start = datetime.now()
    url = 'http://www.dns-shop.ru/catalog/recipe/0dd5516c359be6d4/topovye-processory/'
    all_links = get_all_links( get_html(url))

    for i in all_links:
        print(i)

    #for url in all_links:
    #    html = get_html(url)
    #    data = get_page_data(html)
    #    write_csv(data)

    with Pool(20) as p:
        p.map(make_all, all_links)

    end = datetime.now()

    total = end -start
    print(str(total))

if __name__ == '__main__':
    main()
