from django.shortcuts import render, redirect
from usuarios.validation import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from random_username.generate import generate_username

def cadastro_candidato(request):
    
    """Cadastro de candidatos a vagas."""

    if request.method == 'POST':

        username = generate_username()
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        email = request.POST['email']
        senha = request.POST['senha']
        senha_confirmacao = request.POST['senha2']

        # Validações para efetuar o cadastro:

        if valida_cadastro_nome(request, nome, sobrenome):
            return redirect('cadastro_candidato')
        if valida_cadastro_email(request, email):
            return redirect('cadastro_candidato')
        if valida_cadastro_senha(request, senha, senha_confirmacao):
            return redirect('cadastro_candidato')
        if valida_conflito_email(request, email):
            return redirect('cadastro_candidato')

        # Salvando o usuário no banco de dados:
        
        user = User.objects.create_user(
            username = username,
            first_name = nome, 
            last_name = sobrenome,
            email = email,
            password = senha
        )
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login_candidato')
    else:
        return render(request, 'cadastro_candidato.html')

def login_candidato(request):
    
    """Login de candidatos."""

    if request.method == 'POST':
        
        email = request.POST['email']
        senha = request.POST['senha']

        # Valida e loga o usuário:

        if User.objects.filter(email=email).exists():
            usuario = User.objects.filter(email=email).values_list('username', flat=True).get()
            autenticacao = authenticate(request, username=usuario, password=senha)
            if autenticacao is not None:
                login(request, autenticacao)
                return redirect('dashboard')
            messages.error(request, 'Email ou senha incorretos!')
            return redirect('login_candidato')
        
        return render(request, 'login_candidato.html')
    else:
        return render(request, 'login_candidato.html')

def dashboard(request):

    return render(request, 'dashboard.html')