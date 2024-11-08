from django.db import models

class Ingresso(models.Model):
    nome = models.CharField('Insira a forma de ingresso', max_length=250)

    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.nome