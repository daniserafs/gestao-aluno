from django.views import View
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
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
    

class CadastroCursoView(View):
    formClass = CursoForm
    nomeTemplate = 'CadastroCurso.html'
    
    def get(self, request):
        form = CursoForm()
        context = {
            'form':form
        }
        return render(request, self.nomeTemplate, context=context)


    def post(self, request):
        form = self.formClass(request.POST, request.FILES)
        if form.is_valid():
            print(f'Request: {request.POST}')
            messages.success(request,'Curso cadastrado com sucesso.')
            form.save()
            return HttpResponseRedirect('/cadastro_curso/')
        else:
            messages.error(request, 'Erro ao cadastrar curso.')
            print(forms.errors)
        context = {
            'form':form
        }
        return render(request, self.nomeTemplate, context=context)  