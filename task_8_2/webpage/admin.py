from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import CryptoCurrency, CryptoCurrency_table # наша модель из blog/models.py

admin.site.register(CryptoCurrency)
admin.site.register(CryptoCurrency_table)