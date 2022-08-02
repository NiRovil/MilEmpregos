from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('vagas.urls')),
    path('', include('usuarios.urls')),
    path('admin/', admin.site.urls),
]
