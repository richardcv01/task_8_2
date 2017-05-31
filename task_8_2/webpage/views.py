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
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from .Forms import AuthenticateForm, UserCreateForm
from django_pandas.io import read_frame

from .select_pandas import fun

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

@login_required(login_url="/login/")
def analitic_page(request):
    table = CryptoCurrency_table.pdobjects.filter(price__gt=1).filter(marcet_cap__gt=1)
    df = table.to_dataframe()
    df = df.groupby(df['cryptoCurrency']).max()
    print(df['cryptoCurrency'])
    json = df.to_json(orient='records')
    dic = {'data':json,
           }
    return render(request, 'webpage/analitic_page.html', dic)

class RegisterFormView(FormView):
    form_class = UserCreateForm
    success_url = "/login/"
    template_name = "webpage/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

class LoginFormView(FormView):
    form_class = AuthenticateForm
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



