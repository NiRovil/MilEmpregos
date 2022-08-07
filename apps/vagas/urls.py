from django.urls import path
from vagas import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vagas/', views.cria_vagas, name='vagas'),
    path('vagas-disponiveis/', views.vagas_disponiveis, name='vagas_disponiveis'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('atualizar-vaga/<int:vaga_id>', views.editar_vagas, name='editar_vagas'),
    path('deletar-vaga/<int:vaga_id>', views.deletar_vagas, name='deletar_vagas'),
    path('atualizar', views.atualizar_vaga, name='atualizar_vaga'),
    path('informacoes-vaga/<int:vaga_id>', views.informacoes_vaga, name='informacoes_vaga'),
    path('candidatura/<int:vaga_id>/<int:candidato_id>', views.candidatura, name='candidatura'),
    path('confirmacao/', views.confirma_candidatura, name='confirmacao')
]
