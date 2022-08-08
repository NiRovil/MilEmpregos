from django.db import models
from django.contrib.auth.models import User

class Vagas(models.Model):
    
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
    
    empresa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_vaga = models.CharField(max_length=50, blank=False)
    faixa_salarial = models.CharField(choices=SALARIOS,max_length=2 , blank=False, default='1K')
    escolaridade = models.CharField(choices=ESCOLARIDADES,max_length=2 , blank=False, default='EF')

    def __str__(self):
        return self.nome_vaga

class Candidaturas(models.Model):

    vaga = models.ForeignKey(Vagas, on_delete=models.CASCADE)
    candidato = models.IntegerField()