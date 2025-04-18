from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserForm ,CustomUserLogin
from django.contrib.auth import get_user_model
from django.contrib.auth import logout

User = get_user_model()
def home(request):
    form_register = CustomUserForm()
    form_login = CustomUserLogin()
    return render(request, "user/home.html",{"form_register": form_register,"form_login":form_login})

def login_user(request):
    if request.method == 'POST':
        print(111111111)
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            print(user)
            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password')
            return redirect(request.META.get('HTTP_REFERER', '/'))

    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('home')
        else:
            for field in form.errors:
                messages.error(request, form.errors[field][0])
            return redirect(request.META.get('HTTP_REFERER', '/'))
    return redirect('home')

def logout_user(request):
    if(logout(request)):
        return redirect('home')
    return redirect('home')
