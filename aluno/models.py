from django.db import models

class Aluno(models.Model):
    opcao_campus = ['Araguaína', 'Arraias', 'Gurupi', 'Miracema', 'Palmas', 'Porto Nacional', 'Tocantinópolis']
    opcao_situacao = ['Vinculado', 'Formado', 'Jubilado', 'Evadido']
    opcao_ingresso = ['Vestibular', 'SISU', 'PSEnem']

    aluno_id = models.AutoField(primary_key=True)
    nome_completo = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    matricula = models.IntegerField()
    curso = models.CharField(max_length=100)
    # campus = models.CharField(max_length=1, choices=opcao_campus)
    data_de_nascimento = models.DateField()
    #foto = models.ImageField()
    #situacao = models.CharField(max_length=1, choices=opcao_situacao)
    #forma_de_ingresso = models.CharField(max_length=1, choices=opcao_ingresso)

    def __init__(self, cpf):
        cpf = str(cpf)
        if self.validar_cpf(cpf):
            self.cpf = cpf
        else:
            raise ValueError("CPF é inválido")

    def __str__(self):
        return self.format_cpf()
    
    def validar_cpf(self, cpf):
        cpf = self.cpf
        numeros = [int(digito) for digito in cpf if digito.isdigit()]
        validacao1 = False
        validacao2 = False
        quant_digitos = False

        if len(cpf) == 11:
            quant_digitos = True

            soma_produtos = sum(a*b for a, b in zip(numeros[0:9], range(10, 1, -1)))
            digito_esperado = (soma_produtos * 10 % 11) % 10
            if cpf[9] == digito_esperado:
                validacao1 = True
            
            soma_produtos1 = sum(a*b for a, b in zip(numeros[0:10], range(11, 1, -1)))
            digito_esperado1 = (soma_produtos1 * 10 % 11)%10
            if cpf[10] == digito_esperado1:
                validacao2 = True
            
            if quant_digitos == True and validacao1 == True and validacao2 == True:
                print(f'O CPF {cpf} é válido')
            else: print (f'O CPF {cpf} é inválido')
        else:
            return False
        
    def format_cpf(self):
        fatia_um = self.cpf[:3]
        fatia_dois = self.cpf[3:6]
        fatia_tres = self.cpf[6:9]
        fatia_quatro = self.cpf[9:]
        return(
            "{}.{}.{}-{}".format(
                fatia_um,
                fatia_dois,
                fatia_tres,
                fatia_quatro
                )    
            )