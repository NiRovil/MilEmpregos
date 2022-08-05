from datetime import date
from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):

    usuario_empresa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_empresa = models.CharField(max_length=30)

    def __str__(self):
        return self.nome_empresa

class Candidato(models.Model):

    SALARIOS = (
        ('1K', 'Até 1.000'),
        ('2K', 'De 1.000 à 2.000'),
        ('3K', 'De 2.000 à 3.000'),
        ('4K', 'Acima de 3.000')
    )

    ESCOLARIDADES = (
        ('EF', 'Ensino Fundamental'),
        ('EM', 'Ensino Médio'),
        ('TC', 'Tecnólogo'),
        ('ES', 'Ensino Superior'),
        ('PG', 'Pós / MBA / Mestrado'),
        ('DT', 'Doutorado')
    )

    usuario_candidato = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_candidato = models.CharField(max_length=30)
    pretensao_salarial = models.CharField(choices=SALARIOS, max_length=2, blank=False, default='1K')
    escolaridade = models.CharField(choices=ESCOLARIDADES, max_length=2, blank=False, default='EF')

    def __str__(self):
        return self.nome_candidato

class Experiencia(models.Model):

    usuario_experiencia = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa_anterior = models.CharField(max_length=100)
    emprego_atual = models.BooleanField(default=False)
    data_inicio = models.DateField()
    data_fim = models.DateField(default='9999-12-31')
    descricao = models.TextField()

    def __str__(self):
        return self.empresa_anterior