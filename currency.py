import requests
from bs4 import BeautifulSoup


def parse_values():
    """
    return tuple of tuples in order interbank,black_store,bitok
    with two values buy and sell, except bitok that return values in dollar,UAH
    """
    response = requests.get('https://minfin.com.ua/')
    soup = BeautifulSoup(response.text, "lxml")

    buy = [i.text.split()[0] for i in soup.find_all('span', {'class': 'mf-currency-bid'})]
    sell = [i.text.split()[0] for i in soup.find_all('span', {'class': 'mf-currency-ask'})]
    return tuple(zip(buy, sell))


def get_interbank():
    inter_buy, inter_sell = parse_values()[0]
    return f'Покупка : {inter_buy} -- Продаж : {inter_sell}'


def get_black_store():
    black_buy, black_sell = parse_values()[1]
    return f'Покупка : {black_buy} -- Продаж : {black_sell}'


def get_bitcoin():
    bit_dollar, bit_UAH = parse_values()[2]
    return f'Долар -- {bit_dollar}, Гривня -- {bit_UAH}'
