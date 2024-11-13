from django.urls import path
from academico.views import CadastroView

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('cadastro/', views.CadastroView.as_view(), name='cadastro'),
]