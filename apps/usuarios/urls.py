from django.urls import path
from usuarios import views

urlpatterns = [
    path('cadastro-candidato/', views.cadastro_candidato, name='cadastro_candidato'),
    path('login-candidato/', views.login_candidato, name='login_candidato')
]
