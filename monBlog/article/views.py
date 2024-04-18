from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Article
from .forms import Create_article_form, Create_author_form

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

def article_one(request, id):
    try:
        article = get_object_or_404(Article, id=id)
        return render(request, 'article_one.html', {'article': article})
    except Article.DoesNotExist:
        return render(request, 'article_one.html', {'article': None})

def article_create(request):
    if request.method == 'POST':
        form = Create_article_form(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            content = form.cleaned_data['content']
            form.save()
            return redirect('article_list')
    else:
        form = Create_article_form()
    return render(request, 'article_create.html', {'form': form})

def author_create(request):
    if request.method == 'POST':
        form = Create_author_form(request.POST)
        if form.is_valid():
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            form.save()
            return redirect('article_list')
    else:
        form = Create_author_form()
    return render(request, 'author_create.html', {'form': form})