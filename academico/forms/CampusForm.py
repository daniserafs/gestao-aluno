from django.forms import forms
from academico.models import Campi

class CampusForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Nome do Campus',
        'maxLength':250
    }),
    label = 'Nome do Campus',
    error_messages ={'unique':'Este campus já foi cadastrado!'}),
    

    class Meta:
        model = Campi
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder':'Nome do Campus'
            }),
        }
    
    