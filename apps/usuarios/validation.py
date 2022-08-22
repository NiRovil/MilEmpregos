from django.contrib import messages
from django.contrib.auth.models import User

def valida_cadastro_nome(request, nome, sobrenome):

    """Verifica se o campo nome está em branco."""

    if not nome.strip() or not sobrenome.strip(): 
        messages.error(request, 'Campo nome e sobrenome não pode estar em branco!')
        return True

def valida_cadastro_email(request, email):

    """Verifica se o campo email está em branco."""

    if not email.strip():
        messages.error(request, 'Campo email não pode estar em branco!')
        return True

def valida_cadastro_senha(request, senha, senha_confirmacao):

    """Verifica se as senhas informadas são diferentes."""

    if senha != senha_confirmacao:
        messages.error(request, 'As senhas não coincidem!')
        return True

def valida_conflito_email(request, email):

    """Verifica se já não há nenhum cadastro com o email informado."""

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já cadastrado!')
        return True