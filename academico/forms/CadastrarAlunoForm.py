from django import forms
from academico.models import Aluno

class CadastrarAlunoForm(forms.ModelForm):
    cpf = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Somente números',
        'maxLength':11
    }),
    label = 'CPF do Aluno',
    error_messages ={'unique':'Este CPF já foi cadastrado!'}),

    class Meta:
        model = Aluno
        fields = ['nome','cpf', 'curso', 'dataNascimento', 'foto', 'situacao','formaIngresso', ]
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder':'Nome completo'
            }),
            'dataNascimento': forms.DateInput(attrs={
                'type':'date'
            }),
            'curso':forms.Select(attrs={
                'class':'form-control'
            }),
            'situacao': forms.Select(attrs={
                'class': 'form-control'
            }),
            'formaIngresso':forms.Select(attrs={
                'class':'form-control'
            }),
    
        }
    

