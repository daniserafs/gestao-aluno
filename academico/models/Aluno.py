from django.db import models
from .Ingresso import Ingresso
from .Campi import Campi
from .Situacao import Situacao
from .Curso import Curso

#OPCAO_DE_SITUACAO = ['Vinculado', 'Formado', 'Jubilado', 'Evadido']


class Aluno(models.Model):
    
    nome = models.CharField('Nome Completo do Aluno', max_length=200, help_text='Insira o nome completo do aluno')
    cpf = models.CharField('CPF do aluno', max_length=11, help_text='Insira apenas os números sem caracteres especiais')
    matricula = models.IntegerField(max_length=9)
    dataNascimento = models.DateField() 
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    #foto = models.ImageField()
    situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE)
    campus = models.ForeignKey(Campi, on_delete=models.CASCADE)
    formaIngresso = models.ForeignKey(Ingresso, on_delete=models.CASCADE)
    anoIngresso = models.CharField('Insira o ano de ingresso do aluno',max_length=4)
    
    def __str__(self):

        return self.nome