from django.db import models

class Ingresso(models.Model):
    nome = models.CharField('Forma de ingresso', max_length=250, help_text='Insira a forma de ingresso do aluno')


    class Meta: 
        verbose_name = 'Forma de Ingresso'
        verbose_name_plural = 'Formas de Ingresso'
        
    def __str__(self):
        return self.nome
    