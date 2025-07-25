from django.shortcuts import render
from projetos.models import Projeto

# Create your views here.

def projeto_index(request):
    projetos = Projeto.objects.filter(publicado=True)
    quantidade = projetos.count()
    
    context = {
        'projetos': projetos,
        'quantidade': quantidade,
    }

    return render(request, 'projetos/index.html', context)

def projetos_detalhe(request, pk):
    projeto = Projeto.objects.get(pk=pk)
    context = {
        'projeto': projeto
    }

    return render(request, 'projetos/detalhe.html', context)