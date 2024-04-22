from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from .forms import Create_article_form, Create_author_form, Update_article_form
from django.db.models import Q

def article_list(request):
    query = request.GET.get('book_list', '')
    if query:
        articles = Article.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )
    else:
        articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

def article_one(request, id):
    try:
        article = Article.objects.get(id=id)
        return render(request, 'article_one.html', {'article': article})
    except Article.DoesNotExist:
        return render(request, 'article_one.html', {'article': None})

def article_create(request):
    user = request.user
    if(user.is_authenticated):
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
    else:
        return redirect('login')

def author_create(request):
    user = request.user
    if(user.is_authenticated):
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
    else:
        return redirect('login')


def article_update(request, id):
    user = request.user
    if(user.is_authenticated):
        if request.method == 'POST':
            form = Update_article_form(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                author = form.cleaned_data['author']
                content = form.cleaned_data['content']
                Article.objects.filter(id=id).update(title=title, author=author, content=content)
                return redirect('article_list')
            article = Article.objects.get(id=id)
            form = Update_article_form(instance=article)
            return render(request, 'article_update.html', {'form': form})
        else:
            article = Article.objects.get(id=id)
            form = Update_article_form(instance=article)
            return render(request, 'article_update.html', {'form': form})
    else:
        return redirect('login')


def article_delete(request, id):
    user = request.user
    if(user.is_authenticated):
        if request.method == 'POST':
            Article.objects.filter(id=id).delete()        
            response = HttpResponse('<script>alert("L\'article a été supprimé avec succès."); window.location.href="/";</script>')
            return response
        else:
            return redirect('article_list')
    else:
        return redirect('login')

def article_deleteall(request):
    user = request.user
    if(user.is_authenticated):
        Article.objects.all().delete()
        response = HttpResponse('<script>alert("Tous les articles ont été supprimés avec succès."); window.location.href="/";</script>')
        return response
    else:
        return redirect('login')