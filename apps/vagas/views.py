from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from vagas.models import Vagas
from usuarios.models import Empresa

def index(request):
    return render(request, 'vagas/index.html')

def vagas(request):
    """Criação de vagas para candidatos."""

    if request.method == 'POST':
        empresa = get_object_or_404(Empresa, pk=request.user.id)
        nome_vaga = request.POST['nome_vaga']
        faixa = request.POST['faixa']
        escolaridade = request.POST['escolaridade']

        if nome_vaga == '':
            messages.error(request, 'Nome da vaga inválido!')
            return redirect('vagas')

        vaga = Vagas.objects.create(
            nome_vaga = nome_vaga,
            faixa_salarial = faixa,
            escolaridade = escolaridade
        )

        return render(request, 'dashboard.html')

    return render(request, 'base_vagas.html')