from django.contrib import admin
from ..models import Campi

@admin.register(Campi)
class CampiAdmin(admin.ModelAdmin):
    list_display = ['nome']