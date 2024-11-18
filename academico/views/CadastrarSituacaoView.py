from django.views import View
from django.contrib import messages
from academico.models import Situacao
from .CadastroView import SituacaoForm

class SituacaoForm(SituacaoForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Nome da Situação',
        'maxLength':250
    }),
    label = 'Nome da Situação',
    error_messages ={'unique':'Esta situação já foi cadastrada!'}),
    

    class Meta:
        model = Situacao
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder':'Nome da Situação'
            }),
        }

class CadastrarSituacaoView(View):
    formClass = SituacaoForm
    nomeTemplate = 'CadastrarSituacao.html'
    
    def get(self, request):
        form = SituacaoForm()
        context = {
            'form':form
        }
        return render(request, self.nomeTemplate, context=context)


    def post(self, request):
        form = self.formClass(request.POST, request.FILES)
        if form.is_valid():
            print(f'Request: {request.POST}')
            messages.success(request,'Situação cadastrada com sucesso.')
            form.save()
            return HttpResponseRedirect('/cadastro_situacao/')
        else:
            messages.error(request, 'Erro ao cadastrar situação.')
            print(forms.errors)
        context = {
            'form':form
        }
        return render(request, self.nomeTemplate, context=context)      