import django_tables2 as tables
from .models import CryptoCurrency, CryptoCurrency_table

class Coin_Table(tables.Table):
    id = tables.Column(verbose_name='#')
    class Meta:
        model = CryptoCurrency_table
        exclude = ('insert_date',)
        attrs = {'class': 'paleblue'}