from django.urls import path
from usuarios import views

urlpatterns = [
    path('cadastro-candidato/', views.cadastro_candidato, name='cadastro'),
]
