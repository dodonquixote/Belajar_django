from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *



def login_views(request):
    form = FormLogin()
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/dashboard')
    
    return render(request, 'login/login_views.html', {'form': form})

def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('/login/')
