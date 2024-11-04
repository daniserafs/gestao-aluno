from django.http import HttpResponse

def index(request):
    return HttpResponse('Você está na pagina inicial')