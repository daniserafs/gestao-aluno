from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from gestaoAluno.models import Aluno
# Create your views here.

class AlunoView(View):
    model = Aluno
    
    def get(self, request):
        aluno = self.get(Aluno)
        return HttpResponse('',aluno)

    