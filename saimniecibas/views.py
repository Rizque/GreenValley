from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Saimnieciba
from .forms import UserRegisterForm, ProfileForm
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


def sakumlapa(request):
    return render(request, 'saimniecibas/sakumlapa.html')


class SaimniecibasListView(ListView):
    model = Saimnieciba
    template_name = 'saimniecibas/saimniecibas.html'
    context_object_name = 'saimniecibas'
    ordering = ['-datums']


class SaimniecibaDetailView(DetailView):
    model = Saimnieciba
    template_name = 'saimniecibas/saimnieciba.html'


class SaimniecibaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Saimnieciba
    fields = ['s_nsoaukums', 's_apraksts']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


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


# @login_required
# def profile(request):
#     return render(request, 'saimniecibas/profile.html')


@login_required()
def lietotajaProfils(request):
    profile = request.user

    # skills = profile.skill_set.all()
    # projects = profile.project_set.all()

    context = {'profile': profile, }
    return render(request, 'saimniecibas/profile.html', context)


@login_required()
def redigetProfilu(request):
    profile = request.user
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('profils')
    context = {'form': form}
    return render(request, 'saimniecibas/profile_form.html', context)
