from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer

from .models import CryptoCurrency, CryptoCurrency_table
from django.contrib import auth
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout

@login_required(login_url="/login/")
def index(request):
    select = CryptoCurrency.objects.all()
    if request.method == "POST":
        coin = request.POST['sel']
        if coin != 'All':
            table = CryptoCurrency_table.objects.filter(cryptoCurrency__cryptoCurrency_name__exact=coin)
        else:table = CryptoCurrency_table.objects.all()[:830]
    else:
        table = CryptoCurrency_table.objects.all()[:830]
    print(auth.get_user(request))
    dic = {'table':table, 'select':select, 'username':auth.get_user(request)}
    return render(request, 'webpage/index.html', dic)

class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "webpage/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "webpage/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


from .serializers import CryptoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def crypt_list(request):
    if request.method == 'GET':
        crypto = CryptoCurrency.objects.all()
        serializer = CryptoSerializer(crypto, many=True)
        return Response(serializer.data)
