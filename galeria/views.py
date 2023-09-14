from django.shortcuts import get_object_or_404, render
from galeria.models import Fotografia


# Create your views here.

def index_galeria(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    return render(request, 'galeria/index.html', {
        "cards": fotografias,
    })


def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)

    return render(request, 'galeria/imagem.html', {
        "fotografia": fotografia,
    })


def buscar(request):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        categora_a_buscar = request.GET['buscar']
        if categora_a_buscar:
            fotografias = fotografias.filter(nome__icontains=categora_a_buscar)

    return render(request, 'galeria/buscar.html', {
        "cards": fotografias,
    })
