from django.urls import path
from django.views.generic import TemplateView
from academico.views import AlunoCreateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('cadastro/', TemplateView.as_view(template_name='CadastrarAluno.html')),
    #path('cadastro/', CadastroView.as_view(), name = 'cadastro'),
    path('cadastro-campus', TemplateView.as_view(template_name='CadastrarCampus.html')),
    path('cadastro-curso/', TemplateView.as_view(template_name='CadastrarCurso.html')),
    path('cadastro-situacao/', TemplateView.as_view(template_name='CadastrarSituacao.html')),
    path('cadastro-forma-ingresso/', TemplateView.as_view(template_name='CadastrarFormaIngresso.html')),
    path('listar-alunos/', TemplateView.as_view(template_name='ListarAlunos.html')),
    #path('listar-alunos/<id:int>', TemplateView.as_view(template_name='ListarAlunos.html')),
    path('cadastrar-aluno/', AlunoCreateView.as_view(), name='cadastrar-aluno' ),
    
    


]