class FormadeIngressoForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Nome da Forma de Ingresso',
        'maxLength':250
    }),
    label = 'Nome da Forma de Ingresso',
    error_messages ={'unique':'Esta forma de ingresso já foi cadastrada!'}),
    

    class Meta:
        model = Situacao
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder':'Nome da Forma de Ingresso'
            }),
        }

class CadastrarFormaIngressoView(View):
    formClass = FormadeIngressoForm
    nomeTemplate = 'CadastrarFormaIngresso.html'
    
    def get(self, request):
        form = FormadeIngressoForm()
        context = {
            'form':form
        }
        return render(request, self.nomeTemplate, context=context)


    def post(self, request):
        form = self.formClass(request.POST, request.FILES)
        if form.is_valid():
            print(f'Request: {request.POST}')
            messages.success(request,'Forma de ingresso cadastrada com sucesso.')
            form.save()
            return HttpResponseRedirect('/cadastro_forma_ingresso/')
        else:
            messages.error(request, 'Erro ao cadastrar forma de ingresso.')
            print(forms.errors)
        context = {
            'form':form
        }
        return render(request, self.nomeTemplate, context=context)  