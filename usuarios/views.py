from django.shortcuts import render, redirect
from usuarios.forms import MyLoginForms, MyCadasterForms

from django.contrib.auth.models import User
from django.contrib import auth, messages


def login(request):
    """Função de login do usuário"""
    form = MyLoginForms()

    if request.method == 'POST':
        form = MyLoginForms(request.POST)

        if form.is_valid():
            username = form['username_login'].value()
            password = form['password'].value()

        user = auth.authenticate(request, username=username, password=password)

        if user:
            auth.login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar o login.')
            return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})


def cadastro(request):
    """Função de cadastro de usuário"""
    form = MyCadasterForms()

    if request.method == 'POST':
        form = MyCadasterForms(request.POST)

        if form.is_valid():
            username = form['username_cadaster'].value()
            email = form['email'].value()
            password1 = form['password1'].value()

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Usuário já cadastrado.')
                return redirect('cadastro')

            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    """Função de logout do usuário"""
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('index')
