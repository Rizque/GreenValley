from django.shortcuts import render
from django.http import HttpResponse
from .models import Saimnieciba


def sakumlapa(request):
    return render(request, 'saimniecibas/sakumlapa.html')


def saimniecibas(request):
    saimniecibas = Saimnieciba.objects.all()
    context = {'saimniecibas': saimniecibas}
    return render(request, 'saimniecibas/saimniecibas.html', context)


def saimnieciba(request, pk):
    saimnieciba_k = Saimnieciba.objects.get(id=pk)
    context = {'saimnieciba': saimnieciba_k}
    return render(request, 'saimniecibas/saimnieciba.html', context)
