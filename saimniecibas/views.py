from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .utils import searchProfiles, paginateProfiles
from django.db.models import Q


def frontPage(request):
    return render(request, 'saimniecibas/sakumlapa.html')


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
    products = profile.product_set.all()
    context = {'profile': profile, 'products': products}
    return render(request, 'saimniecibas/account.html', context)


def profiles(request):
    profiles, search_query = searchProfiles(request)
    profiles = profiles.order_by('-s_datums')
    custom_range, profiles = paginateProfiles(request, profiles, 6)
    context = {'profiles': profiles, 'search_query': search_query,
               'custom_range': custom_range}
    return render(request, 'saimniecibas/saimniecibas.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'saimniecibas/saimnieciba.html', context)


def searchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    profiles = Profile.objects.distinct().filter(
        Q(s_nosaukums__icontains=search_query) |
        Q(lokacija__icontains=search_query))
    return profiles, search_query
