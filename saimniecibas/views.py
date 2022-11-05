from django.shortcuts import render
from django.http import HttpResponse
from .models import Saimnieciba


def saimniecibas(request):
    saimniecibas = Saimnieciba.objects.all()
    content = {'saimniecibas': saimniecibas}

    return render(request, 'saimniecibas/saimniecibas.html', content)
