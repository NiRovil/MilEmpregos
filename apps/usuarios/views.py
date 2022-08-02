from django.shortcuts import render
from usuarios.validation import *

def cadastro_candidato(request):
    
    """Cadastro de candidatos a vagas."""

    if request.method == 'POST':

        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        senha_confirmacao = request.POST['senha2']
        valida_cadastro_nome(request, nome)
        valida_cadastro_email(request, email)
        valida_cadastro_senha(request, senha, senha_confirmacao)
        valida_conflito_email(request, email)
        user = User.objects.create_user(
            username = nome, 
            email = email,
            password = senha
        )
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')
    else:
        return render(request, 'cadastro.html')

def login(request):
    
    """Login de candidatos."""
    
    if request.method == 'POST':
        
        email = request.POST['email']
        senha = request.POST['senha']
        valida_login(request, email, senha)
                