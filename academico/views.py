from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from academico.models import Aluno


# Create your views here.

def index(request):
    return HttpResponse('academico view')

class AlunoView(View):
    model = Aluno
    
    def get(self, request):
        aluno = self.get(Aluno)
        return HttpResponse('',aluno)