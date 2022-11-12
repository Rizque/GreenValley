from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Saimnieciba
from .forms import UserRegisterForm
from django.contrib import messages


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


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'saimniecibas/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'saimniecibas/profile.html')
