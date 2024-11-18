from django.views import View
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
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
            return HttpResponseRedirect('/cadastro_campus/')
        else:
            messages.error(request, 'Erro ao cadastrar campus.')
            print(forms.errors)
        context = {
            'form':form
        }
        return render(request, self.nomeTemplate, context=context)      