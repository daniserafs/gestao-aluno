from django.db import models
import Ingresso, Campi, Situacao

OPCAO_DE_SITUACAO = ['Vinculado', 'Formado', 'Jubilado', 'Evadido']


class Aluno(models.Model):
    
    nome = models.CharField('Nome Completo do Aluno', max_length=200, help_text='Insira o nome completo do aluno')
    cpf = models.CharField('CPF do aluno', max_length=11, help_text='Insira apenas os números sem caracteres especiais')
    matricula = models.IntegerField()
    dataNascimento = models.DateField()
    #foto = models.ImageField()
    situacao = models.Model(Situacao())
    formaIngresso = models.Model(Ingresso())
    ano_ingresso = models.CharField('Insira o ano de ingresso do aluno',max_length=4)
    
    def __str__(self):

        return self.nome, self.cpf, self.matricula, self.dataNascimento, self.foto, self.situacao, self.formaIngresso, self.ano_ingresso