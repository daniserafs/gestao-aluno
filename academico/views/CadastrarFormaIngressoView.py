from django.forms import forms 
from django.views import View
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import FormadeIngressoForm

class CadastrarFormaIngressoView(View):
    formClass = FormadeIngressoForm
    nomeTemplate = 'CadastrarFormaIngresso.html'
    
    def get(self, request):
        form = FormadeIngressoForm()
        context = {
            'form':form
        }
        return render(request, self.nomeTemplate, context=context)


    def post(self, request):
        form = self.formClass(request.POST, request.FILES)
        if form.is_valid():
            print(f'Request: {request.POST}')
            messages.success(request,'Forma de ingresso cadastrada com sucesso.')
            form.save()
            return HttpResponseRedirect('/cadastro_forma_ingresso/')
        else:
            messages.error(request, 'Erro ao cadastrar forma de ingresso.')
            print(forms.errors)
        context = {
            'form':form
        }
        return render(request, self.nomeTemplate, context=context)  