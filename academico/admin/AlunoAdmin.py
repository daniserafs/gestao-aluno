from django.contrib import admin
from ..models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome','matricula', 'cpf', 'curso', 'campus', 'dataNascimento', 'situacao', 'formaIngresso']
    readonly_fields = ['matricula']