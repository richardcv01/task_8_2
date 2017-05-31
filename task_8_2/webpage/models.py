from django.db import models
from django.utils import timezone
#from django.core.urlresolvers import reverse
from rest_framework.reverse import reverse
from django_pandas.managers import DataFrameManager
# Create your models here.

class CryptoCurrency(models.Model):
    class Meta:
        unique_together = (('cryptoCurrency_name', 'cryptoCurrency_symbol'))
    cryptoCurrency_name = models.CharField(max_length=20)
    cryptoCurrency_symbol = models.CharField(max_length=20)

    def __str__(self):
        return self.cryptoCurrency_name


class CryptoCurrency_table(models.Model):
    class Meta:
        ordering = ["-insert_date"]
        verbose_name = 'Coint'

    cryptoCurrency = models.ForeignKey(CryptoCurrency, related_name='coins',on_delete=models.CASCADE)
    marcet_cap = models.DecimalField(max_digits=16, decimal_places=2)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    circulating_supply = models.DecimalField(max_digits=16, decimal_places=2)
    volum = models.DecimalField(max_digits=16, decimal_places=2)
    h1 = models.DecimalField(max_digits=16, decimal_places=2)
    h24 = models.DecimalField(max_digits=16, decimal_places=2)
    d7 = models.DecimalField(max_digits=16, decimal_places=2)
    insert_date = models.DateTimeField(db_index=True, auto_now_add=True)

    objects = models.Manager()
    pdobjects = DataFrameManager()

    def __unicode__(self):
        return '%d: %s' % (self.marcet_cap, self.price)

    def __str__(self):
        return str(self.marcet_cap)






