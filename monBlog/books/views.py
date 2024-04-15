from django.shortcuts import render
from django.http import HttpResponse

books = [
        {'id': 0, 'auteur': 'Orwel', 'titre': '1984'},
        {'id': 1, 'auteur': 'Herbert', 'titre': 'Dune'},
        {'id': 2, 'auteur': 'Tolkien', 'titre': 'Le seigneur des anneaux'},
        {'id': 3, 'auteur': 'Doe', 'titre': 'Django pour les nuls'}]

def book_list(request):
    return render(request, 'book_list.html', {'books' : books})

def book_one(request, id):
    return render(request, 'book_one.html', {'book' : get_book_by_id(id, books)})

def get_book_by_id(id, books):
    for book in books:
        if book["id"] == id:
            return book
    return None