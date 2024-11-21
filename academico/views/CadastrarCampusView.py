from django.views import View
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from academico.forms import CampusForm
from django.forms import forms

class CadastrarCampusView(View):
    formClass = CampusForm
    nomeTemplate = 'CadastrarCampus.html'
    
    def get(self, request):
        form = CampusForm()
        context = {
            'form':form
        }
        return render(request, self.nomeTemplate, context=context)


    def post(self, request):
        form = self.formClass(request.POST, request.FILES)
        if form.is_valid():
            print(f'Request: {request.POST}')
            messages.success(request,'Campus cadastrado com sucesso.')
            form.save()
            return HttpResponseRedirect('/cadastro-campus/')
        else:
            messages.error(request, 'Erro ao cadastrar campus.')
            print(forms.errors)
        context = {
            'form':form
        }
        return render(request, self.nomeTemplate, context=context)      