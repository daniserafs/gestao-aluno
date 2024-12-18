from django.db import models
from .Campi import Campi

class Curso(models.Model):
    nome = models.CharField('Curso', max_length=255, help_text='Insira o nome do curso')
    campus = models.ForeignKey(Campi, on_delete=models.CASCADE, help_text='Escolha o campus em que o curso é ofertado')
    

    class Meta: 
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        
    def __str__(self):
        return self.nome