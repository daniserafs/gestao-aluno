from django.views import View
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms import forms
from academico.forms import CadastroAlunoForm

class CadastroAlunoView(View):
    formClass = CadastroAlunoForm
    nomeTemplate = 'CadastrarAluno.html'
    
    def get(self, request):
        form = CadastroAlunoForm()
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