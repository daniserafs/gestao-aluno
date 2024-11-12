from django.db import models

class Campi(models.Model):
    nome = models.CharField('Campus', max_length=250, help_text='Insira o nome do novo Campus')

    def __str__(self):
        return self.nome