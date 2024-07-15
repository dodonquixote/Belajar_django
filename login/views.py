from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import FormLogin

# Create your views here.
def login_views(request):
    form = FormLogin()
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/login/dashboard')
    
    return render(request, 'login/login_views.html', {'form': form})

def dashboard(request):
    context = {}
    return render(request, 'login/dashboard.html', context)
