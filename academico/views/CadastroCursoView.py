from django.views import View
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms import forms
from forms import CursoForm

class CadastroCursoView(View):
    formClass = CursoForm
    nomeTemplate = 'CadastrarCurso.html'
    
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
            return HttpResponseRedirect('/cadastro-curso/')
        else:
            messages.error(request, 'Erro ao cadastrar curso.')
            print(forms.errors)
        context = {
            'form':form
        }
        return render(request, self.nomeTemplate, context=context)  