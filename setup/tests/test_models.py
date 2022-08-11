from django.test import TestCase
from django.contrib.auth.models import User
from usuarios.models import Empresa, Candidato
from vagas.models import Vagas, Candidaturas

class ModelsTest(TestCase):

    # Definindo os modelos a serem criados:
    def setUp(self):
        
        self.usuario_empresa = User.objects.create(
            username = 'TestCase',
            first_name = 'Test', 
            last_name = 'Case',
            email = 'testcase@email.com',
            password = 1234,
            is_staff = True,
        )

        self.usuario_candidato = User.objects.create(
            username = 'TestCase2',
            first_name = 'Test', 
            last_name = 'Case2',
            email = 'testcase2@email.com',
            password = 1234,
            is_staff = False,
        )

        self.empresa = Empresa.objects.create(
            usuario_empresa = self.usuario_empresa,
            nome_empresa = 'Empresa Test Case'
        )

        self.candidato = Candidato.objects.create(
            usuario_candidato = self.usuario_candidato,
            nome_candidato = 'Candidato Test Case',
        )

    def test_usuario_empresa(self):

        self.assertEqual(self.usuario_empresa.username, 'TestCase')
        self.assertEqual(self.usuario_empresa.first_name, 'Test')
        self.assertEqual(self.usuario_empresa.email, 'testcase@email.com')
        self.assertEqual(self.usuario_empresa.password, 1234)
        self.assertEqual(self.usuario_empresa.is_staff, True)

    def test_usuario_candidato(self):

        self.assertEqual(self.usuario_candidato.username, 'TestCase2')
        self.assertEqual(self.usuario_candidato.first_name, 'Test')
        self.assertEqual(self.usuario_candidato.email, 'testcase2@email.com')
        self.assertEqual(self.usuario_candidato.password, 1234)
        self.assertEqual(self.usuario_candidato.is_staff, False)
       
    def test_empresa(self):

        self.assertEqual(self.empresa.nome_empresa, 'Empresa Test Case')

    def test_candidato(self):

        self.assertEqual(self.candidato.nome_candidato, 'Candidato Test Case')
        self.assertEqual(self.candidato.pretensao_salarial, '1K')
        self.assertEqual(self.candidato.escolaridade, 'EF')