from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form)
            form.cleaned_data['username'].lower()
            form.save()
            return redirect('users')
    return render(request, 'register.html', {'form': RegisterForm})

def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('users')
            else:
                return redirect('login')
    return render(request, 'login.html', {'form': LoginForm})