from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello_world(request):
    html = "<h1> welcome to Django Views</h1>"
    title = "moringa MC 54-58 evening check out"
    # return HttpResponse(html)
    return render(request, 'news_app/index.html', {"title": title})


def hello_world2(request):
    html = "<h1> welcome to Django Views</h1>"
    title = "new path 2"
    # return HttpResponse(html)
    return render(request, 'news_app/index.html', {"title": title})
