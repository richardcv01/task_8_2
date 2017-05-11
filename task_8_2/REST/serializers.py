from rest_framework import serializers
from webpage.models import CryptoCurrency, CryptoCurrency_table

class CryptoSerializer(serializers.ModelSerializer):
    #coins = serializers.StringRelatedField(many=True)
    coin = serializers.SerializerMethodField('get_url')

    def get_url(self, obj):
        id = obj.id
        crypto = CryptoCurrency_table.objects.filter(pk=id)
        return str(crypto)

    class Meta:
        model = CryptoCurrency
        fields = ('id', 'cryptoCurrency_name', 'cryptoCurrency_symbol', 'coin')


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoCurrency_table
        fields = ('id', 'cryptoCurrency', 'marcet_cap', 'price', 'circulating_supply',
                  'volum', 'h1', 'h24', 'd7', 'insert_date')


