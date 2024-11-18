from django.urls import path
from academico.views import CadastroView
from academico.views import CadastrarCampusView
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    #path('', views.index, name='index'),
    path('cadastro/', views.CadastroView.as_view(), name='cadastro'),
    #path('cadastro_campus/', CadastrarCampusView.as_view(), name='cadastro_campus'),
    #path('cadastro_curso/', views.CadastroCursoView.as_view(), name='cadastro_curso'),
    #path('cadastro_situacao/', views.CadastrarSituacaoView.as_view(), name='cadastro_situacao'),
    #path('cadastro_forma_ingresso/', views.CadastrarFormaIngressoView.as_view(), name='cadastro_forma_ingresso'),
    #path('listar_alunos/', views.AlunoListView.as_view(), name='listar_alunos'),


]