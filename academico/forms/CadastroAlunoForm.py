from django.forms import ModelForm
from django import forms
from academico.models import Aluno

class CadastroAlunoForm(ModelForm):
    cpf = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Somente números',
        'maxLength':11
    }),
    label = 'CPF do Aluno',
    error_messages ={'unique':'Este CPF já foi cadastrado!'}),
    situacao = forms.CharField(initial='1', widget=forms.HiddenInput())

    class Meta:
        model = Aluno
        fields = ['nome','cpf', 'curso', 'dataNascimento', 'foto', 'situacao', 'formaIngresso']
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder':'Nome completo'
            }),
            'dataNascimento': forms.DateInput(attrs={
                'type':'date'
            }),
            'situacao':forms.Select(attrs={
                'disabled':'disabled'
            }),
            'curso':forms.Select(attrs={
                'class':'form-control'
            }),
            'formaIngresso':forms.Select(attrs={
                'class':'form-control'
            })
        }