from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from vagas.constantes import SALARIOS, ESCOLARIDADES
from vagas.models import Vagas, Candidaturas
from usuarios.models import Empresa, Candidato
from django.contrib.auth.decorators import login_required

def index(request):

    """Renderiza a pagina index."""

    return render(request, 'index/index.html')

@login_required
def dashboard_candidato(request): 
    
    """Define os itens a serem mostrados na dashboard do candidato."""

    usuario_id = 0
    candidato = []
    candidatos = Candidato.objects.all()

    # Itera sob a instancia de 'Candidato' para identificar se o usuário possui cadastro completo:
    for x in candidatos:
        if x.usuario_candidato_id == request.user.id:
            usuario_id = x.id
            candidato = Candidato.objects.get(id=usuario_id)
    
    # Com base no resultado da iteração retorna suas candidaturas, se houver:
    candidaturas = Candidaturas.objects.filter(candidato=usuario_id)
    vagas = Vagas.objects.all()

    # Define o contexto a ser usado pela pagina HTML:
    contexto = {
        'candidatos':candidatos,
        'candidato':candidato, 
        'vagas':vagas,
        'candidaturas':candidaturas,
        'faixas':SALARIOS, 
        'escolaridades':ESCOLARIDADES
    }

    return render(request, 'dashboard/candidato.html', contexto)

@login_required
def dashboard_empresa(request):
    
    empresa = []
    empresas = Empresa.objects.all()

    # Itera sob a instancia de 'Empresa' para identificar se o usuário possui cadastro completo:
    for x in empresas:
        if x.usuario_empresa_id == request.user.id:
            empresa = Empresa.objects.get(id=x.id)
    
    # Retorna as vagas criadas, se houver:
    vagas = Vagas.objects.filter(empresa_id=request.user.id)
    candidaturas = Candidaturas.objects.all()

    # Define o contexto a ser usado pela pagina HTML:
    contexto = {
        'empresa':empresa, 
        'vagas':vagas,
        'candidaturas':candidaturas,
        'faixas':SALARIOS, 
        'escolaridades':ESCOLARIDADES
    }

    return render(request, 'dashboard/empresa.html', contexto)

@login_required
def cria_vaga(request):
    
    """Criação de vagas para candidatos."""

    if request.method == 'POST':

        # Recupera as informações necessárias para o cadastro completo da vaga:
        empresa = request.user.id
        nome_vaga = request.POST['nome_vaga']
        faixa = request.POST['faixa']
        escolaridade = request.POST['escolaridade']

        # Cria uma vaga no banco de dados:
        vaga = Vagas.objects.create(
            empresa_id = empresa,
            nome_vaga = nome_vaga,
            faixa_salarial = faixa,
            escolaridade = escolaridade
        )

        vaga.save()
        messages.success(request, 'Vaga criada com sucesso!')

        return redirect('dashboard_empresa')

    return render(request, 'vagas/criar.html')

@login_required
def edita_vaga(request, vaga_id):

    """Retorna a vaga selecionada pelo usuário."""

    # Retorna com base na resposta da requisição a vaga à atualizar:
    vaga = get_object_or_404(Vagas, pk=vaga_id)
    contexto = {'vaga':vaga}

    return render(request, 'vagas/atualizar.html', contexto)

def atualiza_vaga(request):
    
    """Atualiza a vaga selecionada."""

    if request.method == 'POST':

        # Recupera as informações necessárias para a atualização da vaga:
        vaga_id = request.POST['vaga_id']
        v = Vagas.objects.get(pk=vaga_id)
        v.nome_vaga = request.POST['nome_vaga']
        v.faixa_salarial = request.POST['faixa']
        v.escolaridade = request.POST['escolaridade']

        v.save()
        messages.success(request, 'Vaga atualizada com sucesso!')
        
        return redirect('dashboard_empresa')

@login_required
def deleta_vaga(request, vaga_id):

    """Deleta a vaga selecionada pelo usuário."""

    # Retorna com base na resposta da requisição a vaga à deletar:
    vaga = get_object_or_404(Vagas, pk=vaga_id)
    vaga.delete()
    messages.success(request, 'Vaga deletada com sucesso!')
    return redirect('dashboard_empresa')

@login_required
def informacao_vaga(request, vaga_id):

    """Retorna as informações da vaga selecionada."""

    # Retorna com base na resposta da requisição as informações da vaga:
    vagas = get_object_or_404(Vagas, pk=vaga_id)
    candidaturas = Candidaturas.objects.filter(vaga_id=vaga_id)
    candidatos = Candidato.objects.all()

    contexto = {
        'vagas':vagas, 
        'candidaturas':candidaturas, 
        'candidatos':candidatos,
        'faixas':SALARIOS,
        'escolaridades':ESCOLARIDADES,
    }

    return render(request, 'vagas/informacao.html', contexto)

@login_required
def vagas_disponiveis(request):

    """Retorna as vagas disponíveis para aplicação."""

    if request.method == 'GET':

        usuario = request.user.id

        vagas = Vagas.objects.all()
        candidatos = Candidato.objects.filter(usuario_candidato_id=usuario)
        empresas = Empresa.objects.filter(usuario_empresa_id=usuario)

        contexto = {
            'vagas':vagas, 
            'faixas':SALARIOS,    
            'escolaridades':ESCOLARIDADES,
            'candidatos':candidatos,
            'empresas':empresas,
        }

        return render(request, 'vagas/disponiveis.html', contexto)

@login_required
def candidatura(request, vaga_id, candidato_id):

    """Busca a vaga selecionada pelo candidato."""

    vaga = get_object_or_404(Vagas, pk=vaga_id)
    candidato = get_object_or_404(Candidato, pk=candidato_id)

    # Filtra as candidaturas já efetuadas.
    candidaturas = Candidaturas.objects.filter(vaga_id=vaga.id, candidato=candidato.id)
    contexto = {'vaga':vaga, 'candidato':candidato, 'candidaturas':candidaturas}

    return render(request, 'vagas/confirmar.html', contexto)

@login_required
def confirma_candidatura(request):

    """Confirma a candidatura na vaga."""

    if request.method == 'POST':
        vaga_id = request.POST['vaga_id']
        candidato_id = request.POST['candidato_id']
        candidatura = Candidaturas.objects.create(
            vaga_id = vaga_id,
            candidato = candidato_id
        )

        candidatura.save()
        messages.success(request, 'Candidatura efetuada com sucesso! Boa sorte!')

        return redirect('dashboard_candidato')

@login_required
def desiste_candidatura(request, candidatura_id):

    """Desiste de uma candidatura selecionada pelo usuário."""

    candidatura = get_object_or_404(Candidaturas, pk=candidatura_id)
    candidatura.delete()
    messages.success(request, 'Candidatura desfeita com sucesso!')
    return redirect('dashboard_candidato')