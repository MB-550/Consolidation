from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm
from django.contrib import messages

def user_login(request):
    """
    Method for rendering a request for user login
    """
    return render(request, 'authentication/login.html')



def authenticate_user(request):
      """
      This method authenticates the user trying to login
      """
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
     """
     This method shows the user that has been logged in
     """
     print(request.user.username)
     return render(request, 'authentication/user.html', {
     "username": request.user.username
     
    })

def register(request):
    """
    This Method registers a new user
    """
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