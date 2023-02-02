from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import UpdateView

from django.contrib.auth import login, authenticate, logout

from .utils import searchProfiles, paginateProfiles


def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'saimniecibas/login_register.html')


def logoutUser(request):
    logout(request)
    messages.success(request, 'User was logged out')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('edit-account')
        else:
            messages.success(
                request, 'An error has occurred during registration')

    context = {'page': page, 'form': form}
    return render(request, 'saimniecibas/login_register.html', context)


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')
    context = {'form': form}
    return render(request, 'saimniecibas/profile_form.html', context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile

    # skills = profile.skill_set.all()
    products = profile.product_set.all()

    context = {'profile': profile, 'products': products}
    return render(request, 'saimniecibas/account.html', context)


def profiles(request):
    profiles, search_query = searchProfiles(request)
    profiles = profiles.order_by('-s_datums')

    custom_range, profiles = paginateProfiles(request, profiles, 6)
    context = {'profiles': profiles, 'search_query': search_query,
               'custom_range': custom_range}
    # ordering = ['-s_datums']
    return render(request, 'saimniecibas/saimniecibas.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    # topSkills = profile.skill_set.exclude(description__exact='')
    # otherSkills = profile.skill_set.filter(description='')

    context = {'profile': profile}
    return render(request, 'saimniecibas/saimnieciba.html', context)
# def sakumlapa(request):
#     return render(request, 'saimniecibas/sakumlapa.html')


# def saimniecibas(request):
#     saimniecibas = Profile.objects.all()
#     context = {'saimniecibas': saimniecibas}
#     return render(request, 'saimniecibas/saimniecibas.html', context)


# def saimnieciba(request, pk):
#     saimnieciba_k = Saimnieciba.objects.get(id=pk)
#     context = {'saimnieciba': saimnieciba_k}
#     return render(request, 'saimniecibas/saimnieciba.html', context)


# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(
#                 request, f'Your account has been created! You are now able to log in')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'saimniecibas/register.html', {'form': form})


# @login_required
# def profile(request):
#     return render(request, 'saimniecibas/profile.html')
