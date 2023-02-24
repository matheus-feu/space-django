from django.shortcuts import render, redirect
from django.contrib import messages, auth

from django.contrib.auth.models import User

from django.views.generic import TemplateView
from .forms import MyLoginForms, MyCadasterForms


# Create your views here.
class CadastroView(TemplateView):
    """Cadastra um novo usuário no sistema"""

    def get(self, request, *args, **kwargs):
        """Retorna o formulário de cadastro"""
        form = MyCadasterForms()
        return render(request, 'usuarios/cadastro.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = MyCadasterForms(request.POST)

        username = form['username'].value()
        email = form['email'].value()
        password = form['password'].value()
        password2 = form['password2'].value()

        if form_is_valid(form):
            messages.error(request, 'Erro ao efetuar o cadastro.')
            return redirect('cadastro')

        if campo_vazio(username):
            messages.error(request, 'O campo nome de cadastro não pode ficar em branco.')
            return redirect('cadastro')

        if campo_vazio(email):
            messages.error(request, 'O campo e-mail não pode ficar em branco.')
            return redirect('cadastro')

        if senhas_nao_sao_iguais(password, password2):
            messages.error(request, 'As senhas não são iguais.')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado.')
            return redirect('cadastro')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de cadastro já cadastrado.')
            return redirect('cadastro')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, f'O Usuário(a) {username} foi cadastrado(a) com sucesso.')
        return redirect('login')


class LoginView(TemplateView):
    """Realiza o login do usuário no sistema"""

    def get(self, request, *args, **kwargs):
        """Retorna o formulário de login"""
        form = MyLoginForms()
        return render(request, 'usuarios/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = MyLoginForms(request.POST)

        if not form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(request, username=username, password=password)

            if user:
                auth.login(request, user)
                messages.success(request, f'Usuário(a) {username} logado(a) com sucesso.')
                return redirect('index')
            else:
                messages.error(request, 'Erro ao efetuar o login.')
                return redirect('login')


class LogoutView(TemplateView):
    """Realiza o logout do usuário no sistema"""

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'Usuário deslogado com sucesso.')
        return redirect('login')


def campo_vazio(campo):
    """Verifica se o campo está vazio."""
    return not campo.strip()


def senhas_nao_sao_iguais(password, password2):
    """Verifica se as senhas são iguais."""
    return password != password2


def form_is_valid(form):
    """Verifica se o formulário é válido."""
    return form.is_valid()
