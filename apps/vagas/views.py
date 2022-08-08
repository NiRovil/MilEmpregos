from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from vagas.models import Vagas, Candidaturas
from usuarios.models import Empresa, Candidato

def index(request):
    return render(request, 'vagas/index.html')

def dashboard(request):

    usuario = request.user.id

    candidatos = Candidato.objects.all()
    empresas = Empresa.objects.filter(usuario_empresa_id=usuario)
    vagas = Vagas.objects.all()
    candidaturas = Candidaturas.objects.filter(candidato=usuario)

    FAIXAS = {
        '1K': 'Até 1.000',
        '2K': 'De 1.000 à 2.000',
        '3K': 'De 2.000 à 3.000',
        '4K': 'Acima de 3.000'
    }
    ESCOLARIDADES = {
        'EF': 'Ensino Fundamental',
        'EM': 'Ensino Médio',
        'TC': 'Tecnólogo',
        'ES': 'Ensino Superior',
        'PG': 'Pós / MBA / Mestrado',
        'DT': 'Doutorado'
    }
    contexto = {
        'candidatos':candidatos, 
        'empresas':empresas, 
        'vagas':vagas,
        'candidaturas':candidaturas,
        'faixas':FAIXAS, 
        'escolaridades':ESCOLARIDADES
    }

    return render(request, 'base_dash.html', contexto)

def cria_vagas(request):
    
    """Criação de vagas para candidatos."""

    if request.method == 'POST':
        empresa = request.user.id
        nome_vaga = request.POST['nome_vaga']
        faixa = request.POST['faixa']
        escolaridade = request.POST['escolaridade']

        if nome_vaga == '':
            messages.error(request, 'Nome da vaga inválido!')
            return redirect('vagas')

        vaga = Vagas.objects.create(
            empresa_id = empresa,
            nome_vaga = nome_vaga,
            faixa_salarial = faixa,
            escolaridade = escolaridade
        )

        vaga.save()

        return redirect('dashboard')

    return render(request, 'base_vagas.html')

def editar_vagas(request, vaga_id):

    """Retorna a vaga selecionada pelo usuário."""

    vaga = get_object_or_404(Vagas, pk=vaga_id)
    contexto = {'vaga':vaga}

    return render(request, 'vagas/atualizar_vaga.html', contexto)

def atualizar_vaga(request):
    
    """Atualiza a vaga selecionada."""

    if request.method == 'POST':
        vaga_id = request.POST['vaga_id']
        v = Vagas.objects.get(pk=vaga_id)
        v.nome_vaga = request.POST['nome_vaga']
        v.faixa = request.POST['faixa']
        v.escolaridade = request.POST['escolaridade']

        v.save()

        messages.success(request, 'Vaga atualizada com sucesso!')
        return redirect('dashboard')

def deletar_vagas(request, vaga_id):

    """Deleta a vaga selecionada pelo usuário."""

    vaga = get_object_or_404(Vagas, pk=vaga_id)
    vaga.delete()
    messages.success(request, 'Vaga deletada com sucesso!')
    return redirect('dashboard')

def informacoes_vaga(request, vaga_id):

    """Retorna as informações da vaga selecionada."""

    vaga = get_object_or_404(Vagas, pk=vaga_id)
    candidatos = Candidato.objects.all()
    contexto = {'vaga':vaga, 'candidatos':candidatos}

    return render(request, 'vagas/informacoes_vaga.html', contexto)

def vagas_disponiveis(request):

    """Retorna as vagas disponíveis para aplicação."""

    if request.method == 'GET':

        usuario = request.user.id

        vagas = Vagas.objects.all()
        candidatos = Candidato.objects.filter(usuario_candidato_id=usuario)
        FAIXAS = {
            '1K': 'Até 1.000',
            '2K': 'De 1.000 à 2.000',
            '3K': 'De 2.000 à 3.000',
            '4K': 'Acima de 3.000'
        }
        ESCOLARIDADES = {
            'EF': 'Ensino Fundamental',
            'EM': 'Ensino Médio',
            'TC': 'Tecnólogo',
            'ES': 'Ensino Superior',
            'PG': 'Pós / MBA / Mestrado',
            'DT': 'Doutorado'
        }
        
        contexto = {
            'vagas':vagas, 
            'faixas':FAIXAS,    
            'escolaridades':ESCOLARIDADES,
            'candidatos':candidatos,
        }

        return render(request, 'base_vagas.html', contexto)

def candidatura(request, vaga_id, candidato_id):

    """Busca a vaga selecionada pelo candidato."""

    vaga = get_object_or_404(Vagas, pk=vaga_id)
    candidato = get_object_or_404(Candidato, pk=candidato_id)
    # Filtra as candidaturas já efetuadas.
    candidaturas = Candidaturas.objects.filter(vaga_id=vaga.id, candidato=candidato.id)
    contexto = {'vaga':vaga, 'candidato':candidato, 'candidaturas':candidaturas}

    return render(request, 'vagas/confirmacao.html', contexto)

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

        return redirect('dashboard')

def desistir_candidatura(request, candidatura_id):

    """Desiste de uma candidatura selecionada pelo usuário."""

    candidatura = get_object_or_404(Candidaturas, pk=candidatura_id)
    candidatura.delete()
    messages.success(request, 'Candidatura desfeita com sucesso!')
    return redirect('dashboard')