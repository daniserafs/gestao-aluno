from django.urls import path
from django.views.generic import TemplateView
from academico.views import CadastroView
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('cadastro/', TemplateView.as_view(template_name='cadastrarAluno.html')),
    #path('cadastro/', CadastroView.as_view(), name = 'cadastro'),
    path('cadastro-campus', TemplateView.as_view(template_name='cadastrarCampus.html')),
    path('cadastro-curso/', TemplateView.as_view(template_name='cadastrarCurso.html')),
    path('cadastro-situacao/', TemplateView.as_view(template_name='cadastrarSituacao.html')),
    path('cadastro-forma-ingresso/', TemplateView.as_view(template_name='cadastrarFormaIngresso.html')),
    path('listar-alunos/', TemplateView.as_view(template_name='listarAlunos.html')),


]