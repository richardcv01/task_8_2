from .serializers import CryptoSerializer, DataSerializer, CryptoSerializerAll
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, detail_route, list_route, authentication_classes
from webpage.models import CryptoCurrency, CryptoCurrency_table
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets


class Crypt_ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CryptoCurrency.objects.all()
    serializer_class = CryptoSerializer


class Data_ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CryptoCurrency_table.objects.all()
    serializer_class = DataSerializer


class Crypto_ViewSetAll(viewsets.ReadOnlyModelViewSet):
    queryset = CryptoCurrency_table.objects.all()
    serializer_class = CryptoSerializerAll



class Crypt_List(generics.ListCreateAPIView):
    queryset = CryptoCurrency.objects.all()
    serializer_class = CryptoSerializer



class Cript_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CryptoCurrency.objects.all()
    serializer_class = CryptoSerializer


class Data_List(generics.ListCreateAPIView):
    queryset = CryptoCurrency_table.objects.all()
    serializer_class = DataSerializer

class Data_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CryptoCurrency_table.objects.all()
    serializer_class = DataSerializer

def data_detail(request, pk):
    queryset = CryptoCurrency_table.objects.filter(pk=pk)
    serializer_class = DataSerializer(queryset, many=True)
    return Response(serializer_class.data)



