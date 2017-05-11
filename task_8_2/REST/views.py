from .serializers import CryptoSerializer, DataSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from webpage.models import CryptoCurrency, CryptoCurrency_table
from rest_framework import permissions

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def crypt_list(request):
    if request.method == 'GET':
        crypto = CryptoCurrency.objects.all()
        serializer = CryptoSerializer(crypto, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def cript_detail(request, pk):
    if request.method == 'GET':
        cript = CryptoCurrency_table.objects.get(pk=pk)
        data = CryptoCurrency_table.objects.filter(cryptoCurrency__cryptoCurrency_name__exact=cript)
        serializer = DataSerializer(data, many=True)
        return Response(serializer.data)



@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def data_list(request):
    if request.method == 'GET':
        data = CryptoCurrency_table.objects.all()
        serializer = DataSerializer(data, many=True)
        return Response(serializer.data)