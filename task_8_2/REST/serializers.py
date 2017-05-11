from rest_framework import serializers
from webpage.models import CryptoCurrency, CryptoCurrency_table

class CryptoSerializer(serializers.ModelSerializer):
    coins = [serializers.StringRelatedField(many=True)]
    #coins = serializers.HyperlinkedRelatedField(
        #many=True,
        #read_only=True,
        #view_name='data_detail'
    #)



    class Meta:
        model = CryptoCurrency
        fields = ('id', 'cryptoCurrency_name', 'cryptoCurrency_symbol', 'coins')


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoCurrency_table
        fields = ('id', 'cryptoCurrency', 'marcet_cap', 'price', 'circulating_supply',
                  'volum', 'h1', 'h24', 'd7', 'insert_date')


