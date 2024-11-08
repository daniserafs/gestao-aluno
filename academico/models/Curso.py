from django.db import models
from .Campi import Campi

class Curso(models.Model):
    nome = models.CharField('Insira o nome do curso', max_length=255)
    campus = models.ForeignKey(Campi, on_delete=models.CASCADE, help_text='Escolha o campus em que o curso é ofertado')
    
    def __str__(self):
        return self.nome, self.campus
    
