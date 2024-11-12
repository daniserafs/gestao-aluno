from django.contrib import admin
from ..models import Ingresso

@admin.register(Ingresso)
class IngressoAdmin(admin.ModelAdmin):
    list_display = ['nome']