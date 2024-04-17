from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from .forms import Create_article_form

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

def article_create(request):
    if request.method == 'POST':
        form = Create_article_form(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            content = form.cleaned_data['content']
            form.save()
            return render(request, 'article_created.html')
    else:
        form = Create_article_form()
    return render(request, 'article_create.html', {'form': form})