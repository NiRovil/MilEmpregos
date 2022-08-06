from django.urls import path
from usuarios import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('perfil-candidato/', views.perfil_candidato, name='perfil_candidato'),
    path('atualiza-perfil/', views.atualiza_candidato, name='atualiza_candidato'),
    path('experiencia/', views.experiencia, name='experiencia'),
    path('atualiza-experiencia/', views.atualiza_experiencia, name='atualiza_experiencia'),
    path('perfil-empresa/', views.perfil_empresa, name='perfil_empresa'),
    path('atualiza-empresa/', views.atualiza_empresa, name='atualiza_empresa'),
]
