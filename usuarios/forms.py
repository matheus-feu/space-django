from django import forms
from .models import User


class MyLoginForms(forms.Form):
    username_login = forms.CharField(label="Login", required=True, max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ex.: joao.silva'}))

    password = forms.CharField(label="Senha", required=True, max_length=70, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}))


class MyCadasterForms(forms.Form):
    username_cadaster = forms.CharField(label="Nome de cadastro", required=True, max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': 'Ex.: joao.silva'}))

    email = forms.EmailField(label="E-mail", required=True, max_length=100, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'joao.silva@gmail.com'}))

    password1 = forms.CharField(label="Senha", required=True, max_length=70, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}))

    password2 = forms.CharField(label="Confirmar senha", required=True, max_length=70, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Digite sua senha novamente'}))

    class Meta:
        model = User
        fields = ['username_cadaster', 'email', 'password1', 'password2']

    def clean_username_cadaster_1(self):
        username = self.cleaned_data.get('username_cadaster')

        if username:
            username = username.strip()
            if ' ' in username:
                raise forms.ValidationError('O nome de cadastro não pode conter espaços em branco.')
            else:
                return username

    def clean_username_cadaster_2(self):
        username = self.cleaned_data.get('username_cadaster')

        if username:
            if any(char.isdigit() for char in username):
                raise forms.ValidationError('O nome de cadastro não pode conter números.')
            else:
                return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'Já existe um usuário com o email {email}.')

    def clean_password_1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            if len(password1) < 8:
                raise forms.ValidationError('A senha deve conter no mínimo 8 caracteres.')
            else:
                return password1

    def clean_password_2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError('As senhas não conferem.')
            else:
                return password2
