from django.urls import path
from vagas import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vagas/', views.cria_vaga, name='vagas'),
    path('vagas-disponiveis/', views.vagas_disponiveis, name='vagas_disponiveis'),
    path('dashboard-candidato/', views.dashboard_candidato, name='dashboard_candidato'),
    path('dashboard-empresa/', views.dashboard_empresa, name='dashboard_empresa'),
    path('atualizar-vaga/<int:vaga_id>', views.edita_vaga, name='edita_vaga'),
    path('deletar-vaga/<int:vaga_id>', views.deleta_vaga, name='deleta_vaga'),
    path('atualizar', views.atualiza_vaga, name='atualiza_vaga'),
    path('informacoes-vaga/<int:vaga_id>', views.informacao_vaga, name='informacao_vaga'),
    path('candidatura/<int:vaga_id>/<int:candidato_id>', views.candidatura, name='candidatura'),
    path('confirmacao/', views.confirma_candidatura, name='confirmacao'),
    path('desistir-candidatura/<int:candidatura_id>', views.desiste_candidatura, name='desiste_candidatura'),
]
