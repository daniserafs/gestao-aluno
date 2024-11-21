from django.forms import forms
from academico.models import Situacao

class FormadeIngressoForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Nome da Forma de Ingresso',
        'maxLength':250
    }),
    label = 'Nome da Forma de Ingresso',
    error_messages ={'unique':'Esta forma de ingresso já foi cadastrada!'}),
    

    class Meta:
        model = Situacao
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder':'Nome da Forma de Ingresso'
            }),
        }