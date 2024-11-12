from django.db import models

class Situacao(models.Model):
    nome = models.CharField('Situação do aluno', max_length=250, help_text='Insira a nova situação disponível para o aluno')

    def __str__(self):
        return self.nome