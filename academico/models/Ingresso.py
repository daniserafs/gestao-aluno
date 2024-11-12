from django.db import models

class Ingresso(models.Model):
    nome = models.CharField('Forma de ingresso', max_length=250, help_text='Insira a forma de ingresso do aluno')


    def __str__(self):
        return self.nome
    