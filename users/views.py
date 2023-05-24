from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User, Group
from .forms import UserCreationForm, ProfileForm
from .models import Profile

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

            # Save the user without committing to the database
            user.username = user.username.lower()
            user.save()

            # Render a form for the user to select their group
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
        profile.chosen_group = group_name
        profile.save()

        messages.success(request, 'Group has been set successfully!')

        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('home')

    return render(request, 'users/select_group.html')


def frontpage(request):
    return render(request, 'users/frontpage.html')


@login_required(login_url='login')
def profile(request):
    profile = request.user.profile

    context = {'profile': profile, }
    return render(request, 'users/profile.html', context)


@login_required(login_url='login')
def home(request):
    user_profile = request.user.profile
    user_groups = request.user.groups.values_list('name', flat=True)
    if 'client' in user_groups or 'farm' in user_groups:
        return redirect('profile')
    else:
        user = request.user
        return render(request, 'users/select_group.html', {'user_id': user.id})
