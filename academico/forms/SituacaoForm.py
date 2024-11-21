from django.forms import forms
from academico.models import Situacao

class SituacaoForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Nome da Situação',
        'maxLength':250
    }),
    label = 'Nome da Situação',
    error_messages ={'unique':'Esta situação já foi cadastrada!'}),
    

    class Meta:
        model = Situacao
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder':'Nome da Situação'
            }),
        }
