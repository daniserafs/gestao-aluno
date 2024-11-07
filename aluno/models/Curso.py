from django.db import models
import Campi

class Curso(models.Model):
    nome = models.CharField(max_length=250)
    curso = models.Model(Campi())

    def __str__(self):
        return self.nome