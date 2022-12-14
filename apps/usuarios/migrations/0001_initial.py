# Generated by Django 4.0.6 on 2022-08-10 01:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa_anterior', models.CharField(max_length=100)),
                ('emprego_atual', models.BooleanField(default=False)),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField(default='9999-12-31')),
                ('descricao', models.TextField()),
                ('usuario_experiencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=30)),
                ('usuario_empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_candidato', models.CharField(max_length=30)),
                ('pretensao_salarial', models.CharField(choices=[('1K', 'Até 1.000'), ('2K', 'De 1.000 à 2.000'), ('3K', 'De 2.000 à 3.000'), ('4K', 'Acima de 3.000')], default='1K', max_length=2)),
                ('escolaridade', models.CharField(choices=[('EF', 'Ensino Fundamental'), ('EM', 'Ensino Médio'), ('TC', 'Tecnólogo'), ('ES', 'Ensino Superior'), ('PG', 'Pós / MBA / Mestrado'), ('DT', 'Doutorado')], default='EF', max_length=2)),
                ('pontos', models.IntegerField(default=0)),
                ('usuario_candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
