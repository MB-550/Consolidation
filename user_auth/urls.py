from django.urls import path, include
from django.urls import re_path
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('', views.user_login, name='login'),
#path('login/', views.user_login, name='login'),
 path('authenticate_user/', views.authenticate_user,
 name='authenticate_user'),
 path('show_user/', views.show_user , name = 'show_user'),
 path('register/', views.register, name='register')
 
 
]
