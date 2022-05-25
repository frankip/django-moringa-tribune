from django.shortcuts import render
from django.http import HttpResponse

from news_app.models import Articles

# Create your views here.


def hello_world(request):
    html = "<h1> welcome to Django Views</h1>"
    title = "moringa MC 54-58 evening check out"
    
    articles  = Articles.objects.all()
    print(f"article {articles}")
    # return HttpResponse(html)
    return render(request, 'news_app/index.html', {"title": title,"articles": articles })


def hello_world2(request):
    html = "<h1> welcome to Django Views</h1>"
    title = "new path 2"
    # return HttpResponse(html)
    return render(request, 'news_app/index.html', {"title": title})