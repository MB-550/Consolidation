from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
 """
 Takes you to the home page.
 """
 return render(request, "Home.html")

def index(request):
    """
    Takes you to the Index page.
    """
    return render(request, "Index.html")

def OnlineShop(request):
    """
    Takes you to the Online shop page
    """
    return render(request, "Bootstrap.html")

