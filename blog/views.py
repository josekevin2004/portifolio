from django.shortcuts import render
from blog.models import Postagem, Categoria
# Create your views here.
def blog_index(request):
    postagens = Postagem.objects.all().order_by('-criado_em')

    context = {
        'postagem': postagens,
    }

    return render(request, 'blog/index.html', context)

def blog_categoria(request, categoria):
    postagens = Postagem.objects.filter(
        categorias_name_contains=categoria
    ) .order_by('-criado_em')

    context ={
        'categoria': categoria,
        'postagens': postagens
    }

    return render(request, 'blog/categoria.html', context)
