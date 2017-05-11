from rest_framework import serializers
from .models import CryptoCurrency

class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoCurrency
        fields = ('id', 'cryptoCurrency_name', 'cryptoCurrency_symbol')
