from django.shortcuts import render, redirect
from usuarios.validation import *
from usuarios.models import Empresa, Candidato, Experiencia
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_auth, logout as logout_auth
from random_username.generate import generate_username
from django.contrib.auth.decorators import login_required

def cadastro(request):
    
    """Cadastro de usuários."""

    if request.method == 'POST':

        # Gera um usernamer aleatório em seguida, recupera as demais informações
        # para serem salvas no banco de dados:
        username = generate_username()
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        email = request.POST['email']
        senha = request.POST['senha']
        senha_confirmacao = request.POST['senha2']
        usuario = request.POST['usuario']

        # Valida as informações para efetuar o cadastro do usuário:
        if valida_cadastro_nome(request, nome, sobrenome):
            return redirect('cadastro')
        if valida_cadastro_email(request, email):
            return redirect('cadastro')
        if valida_cadastro_senha(request, senha, senha_confirmacao):
            return redirect('cadastro')
        if valida_conflito_email(request, email):
            return redirect('cadastro')

        # Salva o usuário no banco de dados:
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

        # Redireciona o usuário para a tela de login:
        return redirect('login')

    return render(request, 'login_cadastro/cadastro.html')

def login(request):
    
    """Login de usuários."""

    if request.method == 'POST':
        
        # Recupera as informações necessárias para o login:
        email = request.POST['email']
        senha = request.POST['senha']

        # Verifica se o email cadastrado existe no banco de dados:
        if User.objects.filter(email=email).exists():

            # Definindo o email como forma de validação de login:
            usuario = User.objects.filter(email=email).values_list('username', flat=True).get()
            autenticacao = authenticate(request, username=usuario, password=senha)

            # Validando as informações e efetuando o login do usuário:
            if autenticacao is not None:
                login_auth(request, autenticacao)
                if request.user.is_staff:
                    return redirect('dashboard_empresa')
                return redirect('dashboard_candidato')
            messages.error(request, 'Senha incorreta!')
            return redirect('login')

        # Caso o email não seja encontrado, uma mensagem de erro é exibida:
        messages.error(request, 'Usuário não encontrado! Favor, verifique o email ou cadastre-se!')
        return render(request, 'login_cadastro/login.html')
    
    return render(request, 'login_cadastro/login.html')

@login_required
def perfil_candidato(request):

    """Define as informações do perfil do candidato."""

    if request.method == 'POST':

        # Recupera as informações necessárias para o cadastro completo do candidato:
        usuario = request.user.id
        nome_candidato = request.POST['nome_candidato']
        pretensao_salarial = request.POST['faixa']
        escolaridade = request.POST['escolaridade']

        # Cria um candidato no banco de dados:
        candidato = Candidato.objects.create(
            usuario_candidato_id = usuario,
            nome_candidato = nome_candidato,
            pretensao_salarial = pretensao_salarial,
            escolaridade = escolaridade
        )

        candidato.save()

        return redirect('experiencia')

    usuario = request.user.id
    candidatos = Candidato.objects.filter(usuario_candidato_id=usuario)
    contexto = {'candidatos':candidatos}

    return render(request, 'perfil.html', contexto)

@login_required
def atualiza_candidato(request):

    """Atualiza as informações do candidato."""

    if request.method == 'POST':

        # Recupera as informações necessárias para atualizar o candidato:
        usuario = request.user.id
        c = Candidato.objects.get(usuario_candidato_id=usuario)
        c.nome_candidato = request.POST['nome_candidato']
        c.pretensao_salarial = request.POST['faixa']
        c.escolaridade = request.POST['escolaridade']

        c.save()

        return redirect('atualiza_experiencia')

    usuario = request.user.id
    candidatos = Candidato.objects.filter(usuario_candidato_id = usuario)
    contexto = {'candidatos':candidatos}

    return render(request, 'perfil.html', contexto)

@login_required
def experiencia(request):

    """Define a ultima experiência do candidato."""

    if request.method == 'POST':

        # Recupera as informações necessárias para o cadastro da ultima
        # expeiência do candidato:
        usuario = request.user.id
        empresa = request.POST['empresa_anterior']
        emprego_atual = request.POST['emprego_atual']
        data_inicio = request.POST['data_inicio']
        if request.POST['data_fim'] == '':
            data_fim = '9999-12-31'
        else:
            data_fim = request.POST['data_fim']
        descricao = request.POST['descricao']

        # Salva a ultima experiencia no banco de dados:
        experiencia = Experiencia.objects.create(
            usuario_experiencia_id = usuario,
            empresa_anterior = empresa,
            emprego_atual = emprego_atual,
            data_inicio = data_inicio,
            data_fim = data_fim,
            descricao = descricao
        )

        experiencia.save()

        return redirect('dashboard_candidato')

    usuario = request.user.id
    experiencias = Experiencia.objects.filter(usuario_experiencia_id = usuario)
    contexto = {'experiencias':experiencias}
    
    return render(request, 'experiencia.html', contexto)

@login_required
def atualiza_experiencia(request):

    """Atualiza as informações de experiência."""

    if request.method == 'POST':

        # Recupera as informações necessárias para atualizar a ultima
        # experiência do candidato:
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

        return redirect('dashboard_candidato')

    usuario = request.user.id
    experiencias = Experiencia.objects.filter(usuario_experiencia_id = usuario)
    contexto = {'experiencias':experiencias}

    return render(request, 'experiencia.html', contexto)

@login_required
def perfil_empresa(request):

    """Define o nome da empresa."""

    if request.method == 'POST':

        # Recupera as informações necessárias para o cadastro do nome empresarial:
        usuario_empresa = request.user.id
        nome_empresa = request.POST['nome_empresa']

        empresa = Empresa.objects.create(
            usuario_empresa_id = usuario_empresa,
            nome_empresa = nome_empresa
        )

        empresa.save()

        return redirect('dashboard_empresa')
    
    usuario = request.user.id
    empresas = Empresa.objects.filter(usuario_empresa_id=usuario)
    contexto = {'empresas':empresas}
    return render(request, 'perfil.html', contexto)

@login_required
def atualiza_empresa(request):

    """Atualiza o nome da empresa."""

    if request.method == 'POST':

        # Recupera as informações necessárias para atualizar o nome empresarial:
        usuario = request.user.id
        c = Empresa.objects.get(usuario_empresa_id=usuario)
        c.nome_empresa = request.POST['nome_empresa']

        c.save()

        return redirect('dashboard_empresa')

def logout(request):

    """Opção de logout de usuário."""
    
    logout_auth(request)
    return redirect('index')