from django.db.utils import IntegrityError
from scraper import Scraper
from models import CryptoCurrency, CryptoCurrency_table
import time

def insert_crypt_table():
    scrap_dic = Scraper().return_data()
    print(len(scrap_dic['Name']), len(scrap_dic['Symbol']))
    for name, symbol, market_cap, price, circulating_supply, volume, h1, h24, d7 in zip(
            scrap_dic['Name'], scrap_dic['Symbol'],
            scrap_dic['market_cap'], scrap_dic['Price'], scrap_dic['Circulating supply'],
            scrap_dic['Volume'], scrap_dic['h1'], scrap_dic['h24'], scrap_dic['d7']):
        print(symbol, market_cap, price, circulating_supply, volume, h1, h24, d7 )
        try:
            cr = CryptoCurrency.objects.get_or_create(cryptoCurrency_name=name)
            #cr = CryptoCurrency.objects.get_or_up(cryptoCurrency_name=name)
            print(cr)
            t = CryptoCurrency_table.objects.create\
            (   cryptoCurrency_symbol=symbol,
                marcet_cap=market_cap, price=price, circulating_supply=circulating_supply,
                volum=volume,
                h1=h1,
                h24=h24,
                d7=d7,
                cryptoCurrency=cr[0]
            )
            #t.save()
        except (IntegrityError, Exception) as e:
            print(symbol)
            time.sleep(5)
            print(e)

insert_crypt_table()