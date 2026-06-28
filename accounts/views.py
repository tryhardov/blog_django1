from django.shortcuts import render, redirect
from main.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views.decorators.http import require_POST

def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            messages.success(request, 'Аккаунт успешно создан!')
            return redirect('login')
        else:
            messages.error('Повторите попытку, аккаунт создан неправильно')
        
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form' : form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('block_list')
    
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('block_list')


         



