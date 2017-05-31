import pandas as pd
import sqlite3
from .models import CryptoCurrency, CryptoCurrency_table
from django_pandas.io import read_frame
from django_pandas.managers import DataFrameManager

def fun():
    qs = CryptoCurrency_table.pdobjects.filter(price__gt = 1).filter(marcet_cap__gt=1)
    df = qs.to_dataframe()
    #table = CryptoCurrency_table.objects.filter(price__gt = 1).filter(marcet_cap__gt=1)
    #df = read_frame(table)
    df = df.groupby(['cryptoCurrency']).max().sort_values('marcet_cap', ascending=False)
    #table = df.to_

    #print(df.set_index(['cryptoCurrency']).sort_index())
    #print(df)
