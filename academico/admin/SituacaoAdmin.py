from django.contrib import admin
from ..models import Situacao

@admin.register(Situacao)
class SituacaoAdmin(admin.ModelAdmin):
    list_display = ['nome']