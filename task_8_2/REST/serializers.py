from rest_framework import serializers
from webpage.models import CryptoCurrency, CryptoCurrency_table
from rest_framework.reverse import reverse

#class CryptoSerializer(serializers.HyperlinkedModelSerializer):
class CryptoSerializer(serializers.ModelSerializer):
    coins = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='data_detail',)
    #coins = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = CryptoCurrency
        fields = ('id', 'cryptoCurrency_name', 'cryptoCurrency_symbol', 'coins')


class DataSerializer(serializers.ModelSerializer):
#class DataSerializer(serializers.HyperlinkedRelatedField):
    #cryptoCurrency_name = serializers.ModelSerializer
    class Meta:
        model = CryptoCurrency_table
        fields = ('id', 'cryptoCurrency', 'marcet_cap', 'price', 'circulating_supply',
                  'volum', 'h1', 'h24', 'd7', 'insert_date')


class CryptoSerializerForAll(serializers.ModelSerializer):
    class Meta:
        model = CryptoCurrency
        fields = ('cryptoCurrency_name', 'cryptoCurrency_symbol')

class CryptoSerializerAll(serializers.ModelSerializer):
    cryptoCurrency = CryptoSerializerForAll()

    class Meta:
        model = CryptoCurrency_table
        fields = ('id', 'cryptoCurrency', 'marcet_cap', 'price', 'circulating_supply',
                  'volum', 'h1', 'h24', 'd7', 'insert_date')



