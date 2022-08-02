from django.urls import path
from vagas import views

urlpatterns = [
    path('', views.index, name='index'),
]
