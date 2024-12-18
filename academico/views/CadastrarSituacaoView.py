from django.views import View
from django.contrib import messages
from django.forms import forms
from forms import SituacaoForm
from django.shortcuts import render
from django.http import HttpResponseRedirect

class CadastrarSituacaoView(View):
    formClass = SituacaoForm
    nomeTemplate = 'CadastrarSituacao.html'
    
    def get(self, request):
        form = SituacaoForm()
        context = {
            'form':form
        }
        return render(request, self.nomeTemplate, context=context)


    def post(self, request):
        form = self.formClass(request.POST, request.FILES)
        if form.is_valid():
            print(f'Request: {request.POST}')
            messages.success(request,'Situação cadastrada com sucesso.')
            form.save()
            return HttpResponseRedirect('/cadastro_situacao/')
        else:
            messages.error(request, 'Erro ao cadastrar situação.')
            print(forms.errors)
        context = {
            'form':form
        }
        return render(request, self.nomeTemplate, context=context)      