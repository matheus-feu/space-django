from django import forms
from .models import User


class MyLoginForms(forms.Form):
    username = forms.CharField(label="Login", required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: joao.silva'}))

    password = forms.CharField(label="Senha", required=True, max_length=70, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}))

class MyCadasterForms(forms.Form):
    username = forms.CharField(label="Nome de cadastro", required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'joao.silva'}))

    email = forms.EmailField(label="E-mail", required=True, max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'joao.silva@xpto.com'}))

    password = forms.CharField(label="Senha", required=True, max_length=70, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}))

    password2 = forms.CharField(label="Confirmar senha", required=True, max_length=70, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha novamente'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
