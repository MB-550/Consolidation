from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
 return render(request, "Home.html")

def index(request):
    return render(request, "Index.html")

def OnlineShop(request):
    return render(request, "Bootstrap.html")

