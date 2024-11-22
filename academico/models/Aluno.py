from django.db import models
from .Ingresso import Ingresso
from .Situacao import Situacao
from .Curso import Curso
import datetime


class Aluno(models.Model):
    
    nome = models.CharField('Nome', max_length=200, help_text='Insira o nome completo do aluno')
    cpf = models.CharField('CPF', max_length=11, unique=True,help_text='Insira apenas os números sem caracteres especiais')
    matricula = models.CharField('Matricula',max_length=9, unique=True, editable=False)
    curso = models.ForeignKey(Curso, verbose_name='Curso',on_delete=models.PROTECT)
    dataNascimento = models.DateField('Data de Nascimento') 
    foto = models.ImageField('Insira uma foto do aluno')
    situacao = models.ForeignKey(Situacao, verbose_name='Situação',on_delete=models.PROTECT, default=2, null=True, blank=True)
    formaIngresso = models.ForeignKey(Ingresso, verbose_name='Forma de ingresso',on_delete=models.PROTECT)
    
    def __str__(self):

        return self.nome
    
    class Meta: 
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
    
    def save(self, *args, **kwargs):
        self.gerarMatricula()
        super().save(*args, **kwargs)

    
    def gerarMatricula(self):
        if not self.matricula:
            anoAtual = datetime.datetime.now().year
            semestre = 1 if datetime.datetime.now().month <= 6 else 2

            #existeAluno = Aluno.objects.filter(matricula = self.matricula).exists()
            existeAluno = Aluno.objects.exists()
            if existeAluno:
                ultimaMatricula = Aluno.objects.last().matricula
                ultimoNumero = int(ultimaMatricula[-4:])
            else:
                ultimoNumero = 0
            
            novoNumero = ultimoNumero + 1 

            matricula = f'{anoAtual}{semestre}{novoNumero:04d}'
            self.matricula = matricula
