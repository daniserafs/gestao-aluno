from django.views.generic import CreateView
from academico.models import Aluno
from academico.forms import CadastrarAlunoForm
from django.urls import reverse_lazy

class AlunoCreateView(CreateView):
    model = Aluno
    template_name = 'CadastrarAluno.html'
    form_class = CadastrarAlunoForm
    success_url = reverse_lazy('cadastrar-aluno')

