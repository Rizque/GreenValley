from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User, Group
from .forms import UserCreationForm, ProfileForm, FarmForm
from .models import Profile, Farm, Client
from .utils import searchFarms, paginateFarms


from .decorators import unauthenticated_user


@unauthenticated_user
def loginUser(request):
    page = 'login'
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
            return redirect(request.GET['next'] if 'next' in request.GET else 'home')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'users/login_register.html')


@unauthenticated_user
def registerUser(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')

            user.username = user.username.lower()
            user.save()

            return render(request, 'users/select_group.html', {'user_id': user.id})

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def selectGroup(request):
    if request.method == 'POST':
        group_name = request.POST.get('group')
        user_id = request.POST.get('user_id')

        group = Group.objects.get(name=group_name)
        user = User.objects.get(id=user_id)
        user.groups.add(group)
        user.save()

        profile = Profile.objects.get(user=user)
        profile.username = user.username
        profile.email = user.email
        profile.save()

        if group_name == 'farm':
            Farm.objects.create(owner=profile)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('edit-farm')

        elif group_name == 'client':
            Client.objects.create(person=profile)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('edit-profile')

    return render(request, 'users/select_group.html')


def frontpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'users/frontpage.html')


@login_required(login_url='login')
def profile(request):

    profile = request.user.profile
    group = request.user.groups.all()[0].name
    page = None
    if group == 'farm':
        page = 'farm'
    elif group == 'client':
        page = 'client'

    context = {'profile': profile, 'page': page}
    return render(request, 'users/profile.html', context)


@login_required(login_url='login')
def editProfile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('profile')
    context = {'form': form}
    return render(request, 'users/profile_form.html', context)


@login_required(login_url='login')
def editFarm(request):
    profile = request.user.profile
    farm = profile.farm

    if farm is None:
        farm = Farm(owner=profile)

    form = FarmForm(instance=farm)

    if request.method == 'POST':
        form = FarmForm(request.POST, request.FILES, instance=farm)
        if form.is_valid():
            farm = form.save(commit=False)
            farm.owner = profile
            farm.save()

            return redirect('profile')

    context = {'form': form}
    return render(request, 'users/farm_form.html', context)


@login_required(login_url='login')
def home(request):
    user_profile = request.user.profile
    user_groups = request.user.groups.values_list('name', flat=True)
    if 'client' in user_groups or 'farm' in user_groups:
        return redirect('profile')
    else:
        user = request.user
        return render(request, 'users/select_group.html', {'user_id': user.id})


def farms(request):
    farms, search_query = searchFarms(request)
    farms = farms.order_by('-date')
    custom_range, farms = paginateFarms(request, farms, 6)
    context = {'farms': farms, 'search_query': search_query,
               'custom_range': custom_range}
    return render(request, 'users/farms.html', context)


def farm(request, pk):
    try:
        farm = Farm.objects.get(id=pk)
        latitude = float(farm.latitude) if farm.latitude else None
        longitude = float(farm.longitude) if farm.longitude else None
    except (Farm.DoesNotExist, ValueError):
        farm = None
        latitude = None
        longitude = None

    context = {'farm': farm, 'latitude': latitude, 'longitude': longitude}
    return render(request, 'users/farm.html', context)
