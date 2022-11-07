from django.shortcuts import render
from .models import Produkts


def produkcija(request):
    produkcija = Produkts.objects.all()
    context = {'produkcija': produkcija}
    return render(request, 'produkcija/produkcija.html', context)


def produkts(request, pk):
    produkts_k = Produkts.objects.get(id=pk)
    context = {'produkts': produkts_k}
    return render(request, 'produkcija/produkts.html', context)
