from django.db import models

class Ingresso(models.Model):
    nome = models.CharField('Insira a forma de ingresso', max_length=250)


    def __str__(self):
        return self.nome
    