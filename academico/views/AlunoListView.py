from django.views.generic import ListView
from academico.models import Aluno, Campi, Curso, Ingresso, Situacao

class AlunoListView(ListView):
    model = Aluno
    template_name = 'ListarAlunos.html'
    context_object_name = 'alunos'

    """def get_queryset(self):
        queryset = self.queryset 
        
        if self.kwargs['curso_id']:
            queryset = Aluno.objects.filter(curso__id=self.kwargs['curso_id'])
            campus = self.request.GET.get('campus')
            curso = self.request.GET.get('curso')
            if campus:
                queryset = queryset.filter(campus__id=campus)
            if curso:
                queryset = queryset.filter(curso__id=curso)
         
         
         
        return queryset

        """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['curso'] = Curso.objects.all()
        #context['campus'] = Campi.objects.all()
        context['aluno'] = Aluno.objects.all()
        return context