from django.forms import forms
from academico.models import Curso

class CursoForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Nome do Curso',
        'maxLength':250
    }),
    label = 'Nome do Curso',
    error_messages ={'unique':'Este curso já foi cadastrado!'}),
    campus = forms.ModelChoiceField(queryset=None, widget=forms.Select(attrs={
        'class':'form-control'
    }))

    class Meta:
        model = Curso
        fields = ['nome', 'campus']
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder':'Nome do Curso'
            }),
            'campus':forms.Select(attrs={
                'class':'form-control'
            })
        }
    