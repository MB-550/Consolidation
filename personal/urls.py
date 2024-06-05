from django.urls import path, include
from . import views 
urlpatterns = [
 path('', views.home),
 path('Home.html',views.home),
 path('index.HTML', views.index),
 path('bootstrap.html',views.OnlineShop)
]