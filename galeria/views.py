from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import Fotografia
from django.contrib import messages

def index(request):
    """Função responsável pela exibição da página inicial, carrega todas as imagens publicadas na aplicação,
        se o usuário não estiver logado, redireciona para a página de login"""
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado.')
        return redirect('login')

    fotografias = Fotografia.objects.filter(publicada=True).order_by('-id').all()

    return render(request, 'galeria/index.html', {"cards": fotografias})


def imagem(request, foto_id):
    """Função que exibe uma imagem na página de detalhes, recebe as informações da imagem pelo id"""
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})


def buscar(request):
    """Busca por nome de fotografia e retorna as imagens encontradas na página de busca"""
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado.')
        return redirect('login')

    fotografias = Fotografia.objects.filter(publicada=True).order_by('-id').all()

    if "buscar" in request.GET:
        termo = request.GET['buscar']
        if termo:
            fotografias = fotografias.filter(nome__icontains=termo)

    return render(request, 'galeria/buscar.html', {"cards": fotografias})
