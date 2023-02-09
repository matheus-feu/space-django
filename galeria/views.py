from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia


def index(request):
    """Função responsável pela exibição da página inicial, carrega todas as imagens publicadas na aplicação"""
    fotografias = Fotografia.objects.filter(publicada=True).order_by('-id').all()
    return render(request, 'galeria/index.html', {"cards": fotografias})


def imagem(request, foto_id):
    """Função que exibe uma imagem na página de detalhes, recebe as informações da imagem pelo id"""
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})


def buscar(request):
    """Busca por nome de fotografia e retorna as imagens encontradas na página de busca"""
    fotografias = Fotografia.objects.filter(publicada=True).order_by('-id').all()

    if "buscar" in request.GET:
        termo = request.GET['buscar']
        if termo:
            fotografias = fotografias.filter(nome__icontains=termo)

    return render(request, 'galeria/buscar.html', {"cards": fotografias})
