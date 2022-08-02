from django.contrib import messages
from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def valida_cadastro_nome(request, nome):

    """Verifica se o campo nome está em branco."""

    if not nome.strip():
        messages.error(request, 'Campo nome não pode estar em branco!')
        return redirect('cadastro_candidato')

def valida_cadastro_email(request, email):

    """Verifica se o campo email está em branco."""

    if not email.strip():
        messages.error(request, 'Campo email não pode estar em branco!')
        return redirect('cadastro_candidato')

def valida_cadastro_senha(request, senha, senha_confirmacao):

    """Verifica se as senhas informadas são iguais."""

    if senha != senha_confirmacao:
        messages.error(request, 'As senhas não coincidem!')
        return redirect('cadastro_candidato')

def valida_conflito_email(request, email):

    """Verifica se já não há nenhum cadastro com o email informado."""

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já cadastrado!')
        return redirect('cadastro_candidato')

def valida_login(request, email, senha):

    """Verifica se o email e senha estão sendo preenchidos."""

    if email == "" or senha == "":
        messages.error(request, 'Verifique os campos email e senha!')
        return redirect('login')

def login_candidato(request, email, senha):

    """Valida e loga o usuário."""

    if User.objects.filter(email=email).exists():
        nome = User.objects.filter(email=email).values_list('username', flat=True).get()
        usuario = authenticate(request, username=nome, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect('dashboard')
    return render(request, 'login.html')