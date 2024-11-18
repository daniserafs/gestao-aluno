from django.views import View
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from academico.models import Aluno


class AlunoForm(forms.ModelForm):
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
    

class CadastroView(View):
    formClass = AlunoForm
    nomeTemplate = 'CadastrarAluno.html'
    
    def get(self, request):
        form = AlunoForm()
        context = {
            'form':form
        }
        return render(request, self.nomeTemplate, context=context)


    def post(self, request):
        form = self.formClass(request.POST, request.FILES)
        if form.is_valid():
            print(f'Request: {request.POST}')
            messages.success(request,'Aluno cadastrado com sucesso.')
            form.save()
            return HttpResponseRedirect('/cadastro/')
        else:
            messages.error(request, 'Erro ao cadastrar aluno.')
            print(forms.errors)
        context = {
            'form':form
        }
        return render(request, self.nomeTemplate, context=context)