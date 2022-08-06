from django.urls import path
from vagas import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vagas/', views.cria_vagas, name='vagas'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('atualizar-vaga/<int:vaga_id>', views.editar_vagas, name='editar_vagas'),
    path('atualizar', views.atualizar_vaga, name='atualizar_vaga')
]
