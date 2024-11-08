from django.db import models

class Situacao(models.Model):
    nome = models.CharField('Insira a nova situção', max_length=250, help_text='Insira a nova situação disponivel para o aluno')

    def __str__(self):
        return self.nome