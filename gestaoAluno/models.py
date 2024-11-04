from django.db import models

class Aluno(models.Model):
    opcao_campus = ['Araguaína', 'Arraias', 'Gurupi', 'Miracema', 'Palmas', 'Porto Nacional', 'Tocantinópolis']
    opcao_situacao = ['Vinculado', 'Formado', 'Jubilado', 'Evadido']
    opcao_ingresso = ['Vestibular', 'SISU', 'PSEnem']

    nome_completo = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    matricula = models.IntegerField(max_length=9 )
    curso = models.CharField(max_length=100)
    campus = models.CharField(max_length=1, choices=opcao_campus)
    data_de_nascimento = models.DateField()
    foto = models.ImageField()
    situacao = models.CharField(max_length=1, choices=opcao_situacao)
    forma_de_ingresso = models.CharField(max_length=1, choices=opcao_ingresso)

#def regra_matricula():
        
"""i) gerado automaticamente após o cadastro do aluno utilizando as seguintes regras:
                1) 9 dígitos numéricos
                2) os primeiros 5 dígitos referem-se ao semestre de ingresso. deve considerar o semestre atual do sistema. logo, se estivermos no primeiro semestre do ano, a matrícula deve iniciar com 20231xxxxxx
                3) os demais números da matrícula são sequências
                4) não pode existir uma matrícula repetida"""