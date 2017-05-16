from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from django.db.utils import IntegrityError
from .scraper import Scraper
from .models import CryptoCurrency, CryptoCurrency_table

logger = get_task_logger(__name__)

def insert_crypt_table():
    scrap_dic = Scraper().return_data()
    for name, symbol, market_cap, price, circulating_supply, volume, h1, h24, d7 in zip(
            scrap_dic['Name'], scrap_dic['Symbol'],
            scrap_dic['market_cap'], scrap_dic['Price'], scrap_dic['Circulating supply'],
            scrap_dic['Volume'], scrap_dic['h1'], scrap_dic['h24'], scrap_dic['d7']):
        try:
            pass
            cr = CryptoCurrency.objects.get_or_create(cryptoCurrency_name=name, cryptoCurrency_symbol=symbol)
            t = CryptoCurrency_table.objects.create\
            (
                marcet_cap=market_cap, price=price, circulating_supply=circulating_supply,
                volum=volume,
                h1=h1,
                h24=h24,
                d7=d7,
                cryptoCurrency=cr[0]
            )
            t.save()
        except (IntegrityError, Exception) as e:
            print(e)

@periodic_task(
    run_every=(crontab(minute='*/50')),
    name="task_save",
    ignore_result=True
)
def task_save_table():
    print('start')
    insert_crypt_table()
    print('insert data')
