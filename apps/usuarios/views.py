from django.shortcuts import get_object_or_404, render, redirect
from usuarios.validation import *
from usuarios.models import Empresa
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_auth, logout as logout_auth
from random_username.generate import generate_username

def cadastro(request):
    
    """Cadastro de candidatos a vagas."""

    if request.method == 'POST':

        username = generate_username()
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        email = request.POST['email']
        senha = request.POST['senha']
        senha_confirmacao = request.POST['senha2']
        usuario = request.POST['usuario']

        # Validações para efetuar o cadastro:

        if valida_cadastro_nome(request, nome, sobrenome):
            return redirect('cadastro')
        if valida_cadastro_email(request, email):
            return redirect('cadastro')
        if valida_cadastro_senha(request, senha, senha_confirmacao):
            return redirect('cadastro')
        if valida_conflito_email(request, email):
            return redirect('cadastro')

        # Salvando o usuário no banco de dados:
        
        user = User.objects.create_user(
            username = username,
            first_name = nome, 
            last_name = sobrenome,
            email = email,
            password = senha,
            is_staff = usuario,
        )
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def cadastro_empresa(request):
    """Criando a empresa a partir do usuário."""
    
    if request.method == 'POST':

        nome_empresa = request.POST['empresa_nome']
        usuario = get_object_or_404(User, pk=request.user.id)
        empresa = Empresa.objects.create(
            usuario_empresa = usuario,
            nome_empresa = nome_empresa
        )
        return redirect('dashboard')
    
    return render(request, 'base_perfil.html')

def login(request):
    
    """Login de candidatos."""

    if request.method == 'POST':
        
        email = request.POST['email']
        senha = request.POST['senha']

        # Valida e loga o usuário:

        if User.objects.filter(email=email).exists():
            usuario = User.objects.filter(email=email).values_list('username', flat=True).get()
            autenticacao = authenticate(request, username=usuario, password=senha)
            if autenticacao is not None:
                login_auth(request, autenticacao)
                return redirect('dashboard')
            messages.error(request, 'Email ou senha incorretos!')
            return redirect('login')
        
        return render(request, 'usuarios/login.html')
    else:
        return render(request, 'usuarios/login.html')

def dashboard(request):

    return render(request, 'usuarios/dashboard.html')

def perfil(request):

    return render(request, 'base_perfil.html')