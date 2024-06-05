from django.shortcuts import render

# Create your views here.
def blog(request):
    """
    Takes you to the blog page
    """
    return render(request, "Blog.html")