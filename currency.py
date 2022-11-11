from collections import namedtuple

import requests
from bs4 import BeautifulSoup


def parse_values():
    response = requests.get('https://minfin.com.ua/')
    soup = BeautifulSoup(response.text, "lxml")

    buy = [i.text.split()[0] for i in soup.find_all('span', {'class': 'mf-currency-bid'})]
    sell = [i.text.split()[0] for i in soup.find_all('span', {'class': 'mf-currency-ask'})]

    return namedtuple('Currency', ('inter_bank', 'black_store', 'bitok'))(*zip(buy, sell))


def get_interbank():
    inter_buy, inter_sell = parse_values().inter_bank
    return f'Покупка : {inter_buy} -- Продаж : {inter_sell}'


def get_black_store():
    black_buy, black_sell = parse_values().black_store
    return f'Покупка : {black_buy} -- Продаж : {black_sell}'


def get_bitcoin():
    bit_dollar, bit_UAH = parse_values().bitok
    return f'Долар -- {bit_dollar}, Гривня -- {bit_UAH}'
