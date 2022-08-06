from django.shortcuts import render, redirect
from usuarios.validation import *
from usuarios.models import Empresa, Candidato, Experiencia
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

    return render(request, 'registro/cadastro.html')

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
            messages.error(request, 'Senha incorreta!')
            return redirect('login')

        messages.error(request, 'Usuário não encontrado! Favor, verifique o email ou cadastre-se!')
        return render(request, 'registro/login.html')
    
    return render(request, 'registro/login.html')

def perfil_candidato(request):

    if request.method == 'POST':
        usuario = request.user.id
        nome_candidato = request.POST['nome_candidato']
        pretensao_salarial = request.POST['faixa']
        escolaridade = request.POST['escolaridade']

        candidato = Candidato.objects.create(
            usuario_candidato_id = usuario,
            nome_candidato = nome_candidato,
            pretensao_salarial = pretensao_salarial,
            escolaridade = escolaridade
        )

        candidato.save()

        return redirect('experiencia')

    candidatos = Candidato.objects.all()
    contexto = {'candidatos':candidatos}

    return render(request, 'base_perfil.html', contexto)

def atualiza_candidato(request):

    if request.method == 'POST':
        usuario = request.user.id
        c = Candidato.objects.get(usuario_candidato_id=usuario)
        c.nome_candidato = request.POST['nome_candidato']
        c.pretensao_salarial = request.POST['faixa']
        c.escolaridade = request.POST['escolaridade']

        c.save()

        return redirect('atualiza_experiencia')

    candidatos = Candidato.objects.all()
    contexto = {'candidatos':candidatos}

    return render(request, 'base_perfil.html', contexto)

def experiencia(request):

    if request.method == 'POST':
        usuario = request.user.id
        empresa = request.POST['empresa_anterior']
        emprego_atual = request.POST['emprego_atual']
        data_inicio = request.POST['data_inicio']
        if request.POST['data_fim'] == '':
            data_fim = '9999-12-31'
        else:
            data_fim = request.POST['data_fim']
        descricao = request.POST['descricao']

        experiencia = Experiencia.objects.create(
            usuario_experiencia_id = usuario,
            empresa_anterior = empresa,
            emprego_atual = emprego_atual,
            data_inicio = data_inicio,
            data_fim = data_fim,
            descricao = descricao
        )

        experiencia.save()

        return redirect('dashboard')

    experiencias = Experiencia.objects.all()
    contexto = {'experiencias':experiencias}
    
    return render(request, 'base_experiencia.html', contexto)

def atualiza_experiencia(request):

    if request.method == 'POST':
        usuario = request.user.id
        e = Experiencia.objects.get(usuario_experiencia_id=usuario)
        e.empresa_anterior = request.POST['empresa_anterior']
        e.emprego_atual = request.POST['emprego_atual']
        e.data_inicio = request.POST['data_inicio']
        if request.POST['data_fim'] != '':
            e.data_fim = request.POST['data_fim']
        else:
            e.data_fim = '9999-12-31'
        e.descricao = request.POST['descricao']

        e.save()

        return redirect('dashboard')

    experiencias = Experiencia.objects.all()
    contexto = {'experiencias':experiencias}

    return render(request, 'base_experiencia.html', contexto)

def perfil_empresa(request):

    if request.method == 'POST':
        usuario_empresa = request.user.id
        nome_empresa = request.POST['nome_empresa']

        empresa = Empresa.objects.create(
            usuario_empresa_id = usuario_empresa,
            nome_empresa = nome_empresa
        )

        empresa.save()

        return redirect('dashboard')
    
    empresas = Empresa.objects.all()
    contexto = {'empresas':empresas}

    return render(request, 'base_perfil.html', contexto)

def atualiza_empresa(request):

    if request.method == 'POST':
        usuario = request.user.id
        c = Empresa.objects.get(usuario_empresa_id=usuario)
        c.nome_empresa = request.POST['nome_empresa']

        c.save()

        return redirect('dashboard')
    
    empresas = Empresa.objects.all()
    contexto = {'empresas':empresas}

    return render(request, 'base_perfil.html', contexto)