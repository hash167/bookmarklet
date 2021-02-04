from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, \
                   UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    ctx = {
        'section': 'people',
        'users': users
    }
    return render(request, 'account/user/list.html', ctx)


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    ctx = {
        'section': 'people',
        'user': user
    }
    return render(request, 'account/user/detail.html', ctx)


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user but don't save yet
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


# Not used in favor CBVs in django.contrib.auth.views
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, password=cd['password'], username=cd['username'])
            if user is not None:
                if user.is_active:
                    # the login() method sets the user in the session
                    login(request, user)
                    return HttpResponse('Authenticated sucessfuly')
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse('Invalid login')
    form = LoginForm()
    return render(request, 'account/login.html', {'form': form})



