from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, 'Account was created' + user)
                return redirect('login')
    context = {'form': form}
    return render(request, 'myapp/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'myapp/login.html')


def logoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def profile(request, user_pk):
    try:
        user = get_object_or_404(User, pk=user_pk)
        return render(request, 'myapp/profile.html', {'user': user, 'user_pk': user_pk})
    except User.DoesNotExist:
        return HttpResponse("User does not exist")


@login_required(login_url='login')
def home(request):
    return render(request, 'myapp/home.html')


