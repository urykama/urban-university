import time

import requests
import lxml
from pprint import pprint
from bs4 import BeautifulSoup
# from requests_html import HTMLSession


# Программа должна считывать данные с сайта CoinMarketCap.
def html_to_file(url='https://coinmarketcap.com/ru/'):
    # url = 'https://coinmarketcap.com/ru/'
    response = requests.get(headers=header_of_request, url=url)
    if response.status_code == 200:
        time.sleep(3)
        src = response.text
        with open('index.html', 'w', encoding="utf-8") as file:
            file.write(src)


# Для парсинга и запросов разрешено использовать любую из перечисленных библиотек:
# requests, selenium, beautifulsoup, scrapy.
def query():
    with open('index.html', encoding="utf-8") as file:
        src = file.read()
    response = requests.get(headers=header_of_request, url='https://coinmarketcap.com/')
    if response.status_code == 200:
        # time.sleep(3)
        src = response.text
    # soup = BeautifulSoup(src, features='html.parser')
    soup = BeautifulSoup(src, 'lxml')
    coin_list = soup.findAll('div', {'class': "sc-aef7b723-0 sc-1c5f2868-1 jcJMEg"})
    # coin_list = html.findAll('div', {'class': "sc-aef7b723-0 sc-1c5f2868-2 bhBHDD  hide-ranking-number"})
    coin_list = soup.find_all(class_="sc-aef7b723-0 sc-1c5f2868-2 bhBHDD hide-ranking-number")
    coin_list = soup.find_all(class_="sc-aef7b723-0 sc-1c5f2868-1 jcJMEg")
    coin_list = soup.find_all(class_="sc-7bc56c81-1 bCdPBp")
    coin_list = soup.find_all(class_="sc-7bc56c81-0 dCzASk")
    # coin_list = soup.find_all('div', class_="sc-1c5f2868-3 gJXwZh")
    # coin_list = soup.find_all('span', class_="crypto-symbol")
    for i in coin_list:
        pprint(i)
        pprint(i.text)

        print(i.get_text(strip=True, separator='\n'))
    print(len(coin_list))
    coin_list = soup.find_all('div', class_="sc-1c5f2868-3 gJXwZh")
    # coin_list = soup.find_all('span', class_="crypto-symbol")
    for i in coin_list:
        pprint(i)
        pprint(i.text)

        print(i.get_text(strip=True, separator='\n'))
    print(len(coin_list))
    # Ваш код должен выполнять следующий функционал:
    # Считывать данные с сайта: название криптовалюты, текущая рыночная капитализация
    # Записывать данные в CSV файл в следующем порядке: название криптовалюты, текущая рыночная капитализация,
    # процент от общей капитализации топ-100 криптовалют.
def selen(url):
    s = HTMLSession()
    response = s.get(url)
    response.html.render()

    print(response)
    # prints out the content of the fully loaded page
    # response can be parsed with for example bs4

def query2():
    response = requests.get(headers=header_of_request, url='https://coinmarketcap.com/', timeout=5).text
    soup = BeautifulSoup(response, 'lxml')
    tbody = soup.find('tbody')
    coins = tbody.find_all('tr')
    i = 0
    for coin in coins:
        i += 1
        # name = coin.find(class_='sc-4984dd93-0 iqdbQL coin-item-symbol')
        # name = coin.find(class_='cmc-link').get('href').replace('/currencies/', '')
        name = coin.find(class_='cmc-link').get('href')
        name = coin.find(class_='sc-7bc56c81-1 bCdPBp')
                           # class ="sc-7bc56c81-1 bCdPBp"
        market_cap = coin.find(class_='sc-7bc56c81-1 bCdPBp')
        if name:
            # print(name, '\t',  name.text, '\t',  market_cap.text, '\t', coin)
            print(i, '\t', name, '\t', market_cap.text, '\t', coin)
        else:
            print(i, '\t', coin.find(class_='crypto-symbol').text, '\t', coin)
            print(i, '\t', coin.find_all('td')[-2])
            print(i, '\t', coin.find(class_='sc-7bc56c81-1 bCdPBp'))

def parse_cryptocurrency_links() -> [str]:
    req = requests.get(
        'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=9114&sortBy=market_cap&sortType=desc&convert=USD,BTC,ETH&cryptoType=all&tagType=all&audited=false&aux=ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_30d,self_reported_circulating_supply,self_reported_market_cap')
    data = req.json()

    basis_link = 'https://coinmarketcap.com/ru/currencies/'
    currency_links = []

    for currency in data['data']['cryptoCurrencyList']:
        currency_links.append(f'{basis_link}{currency["slug"]}/')
    return currency_links


def write_cmc_top():
    url = 'https://coinmarketcap.com/'
    # print('111')
    # html_to_file('https://coinmarketcap.com/ru/')
    query()
    # print('*' * 150)
    # html_to_file('https://sensors.saasexch.com/sa.gif?project=cmc')
    # selen(url)
    # query2()
    return


if __name__ == '__main__':
    header_of_request = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "ru,en-US;q=0.9,en;q=0.8,ru-RU;q=0.7",
        "cache-control": "no-cache",
        "dnt": "1",
        "pragma": "no-cache",
        "sec-ch-ua": '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

    write_cmc_top()

# Hello!
# по поводу этого ДЗ:
# ПРАКТИЧЕСКОЕ ЗАДАНИЕ
# 2024/02/10 00:00|Домашнее задание по теме "Парсинг сайтов"
# можно использовать API (у сайта есть API), или нужно парсить без использования API?
# Я тоже в как-то раз пролил кофе (или чай) на клавиатуру.
# Жена аж подпрыгнула от радости: думала я из-за компа вылезу и пойду к ней грустить...
# Я достал со шкафа следующую клавиатуру, и закончили бой победой.