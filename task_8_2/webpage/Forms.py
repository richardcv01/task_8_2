from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms


class AuthenticateForm(AuthenticationForm):
    username = forms.CharField(label='usename' ,widget=forms.widgets.TextInput(attrs={"id":"inputEmail", "class":"form-control", "placeholder":"Usernmae"}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={"id":"inputPassword","class":"form-control",'placeholder': 'Password'}))



class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control",'placeholder': 'Email', "name":"username"}))
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control",'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control",'placeholder': 'Last Name'}))
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={"class":"form-control",'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={"class":"form-control",'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={"class":"form-control",'placeholder': 'Password Confirmation'}))

    class Meta:
        fields = ['email', 'username', 'first_name', 'last_name', 'password1',
                  'password2']
        model = User



