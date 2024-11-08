from django.db import models

class Aluno(models.Model):
    opcao_campus = [
        ('Arg','Araguaína'), 
        ('Ars', 'Arraias'), 
        ('Gur','Gurupi'), 
        ('Mir','Miracema'), 
        ('Pmw','Palmas'), 
        ('Ptn','Porto Nacional'), 
        ('Toc','Tocantinópolis'),
        ]
    opcao_situacao = ['Vinculado', 'Formado', 'Jubilado', 'Evadido']
    opcao_ingresso = ['Vestibular', 'SISU', 'PSEnem']

    
    nomeCompleto = models.CharField('insira o nome completo',max_length=200)
    cpf = models.CharField(max_length=11)
    matricula = models.IntegerField()
    curso = models.CharField('Insira o nome do curso',max_length=100)
    #campus = models.CharField(max_length=1, choices=opcao_campus)
    data_de_nascimento = models.DateField()
    #foto = models.ImageField() ->instalar pillow
    #situacao = models.CharField(max_length=1, choices=opcao_situacao)
    #forma_de_ingresso = models.CharField(max_length=1, choices=opcao_ingresso)

    def __str__(self):
        return self.nomeCompleto