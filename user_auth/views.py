from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm
from django.contrib import messages

def user_login(request):
 return render(request, 'authentication/login.html')



def authenticate_user(request):
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username=username, password=password)
      if user is None:
          return HttpResponseRedirect(
          reverse('user_auth:login')
          )
      else:
          login(request, user)
          return HttpResponseRedirect(
          reverse('user_auth:show_user')
          )

def show_user(request):
     print(request.user.username)
     return render(request, 'authentication/user.html', {
     "username": request.user.username,
     "password": request.user.password
    })

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('user_auth:login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'authentication/register.html', context)