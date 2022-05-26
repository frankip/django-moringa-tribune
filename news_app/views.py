from django.shortcuts import redirect, render
from django.http import HttpResponse

from news_app.models import Articles
from news_app.forms import ArticleForms

# Create your views here.


def hello_world(request):
    form = ArticleForms()
    
    if request.method == "POST":
        form = ArticleForms(request.POST)
        if form.is_valid():
            # save instance
            pass
        
    else:
        form = ArticleForms()
        
    title = "moringa MC 54-58 evening check out"
    articles  = Articles.objects.all()
    
    ctx = {
        "title": title,
        "articles": articles,
        "form": form
    }
    
    return render(request, 'news_app/index.html', ctx)


def hello_world2(request):
    html = "<h1> welcome to Django Views</h1>"
    title = "new path 2"
    # return HttpResponse(html)
    return render(request, 'news_app/index.html', {"title": title})


def add_articles(request):
    form = ArticleForms()
    
    if request.method == 'POST':
        form = ArticleForms(request.POST)
        print(f'articleforms == {form}')
        
        if form.is_valid():
            form.save()
            
            return redirect('/')
        
    else:      
        ctx= {
            "form": form
        }
        return render(request, 'news_app/add_article.html', ctx)