from books_authers_app.models import Books
from django.shortcuts import redirect, render
from .models import *

from django.shortcuts import render, HttpResponse


def index(request):
    context = {
        'all_books': allbooks()
    }
    return render(request, 'AddBook.html', context)


def create_book(request):
    if request.method == 'POST':
        data = request.POST
        createbook(data)
    return redirect('/')


def show_book(request, id):
    context = {'book': showbook(id),
               'authers': bookauthers(id),
               'allauthers': allauthers()
               }
    return render(request, 'ShowBook.html', context)


def add_auther_to_book(request):
    if request.method == 'POST':
        data = request.POST
        print(data['bookid'])
        print('data'*30)
        print(data['autherinfo'])
        thisbook = showbook(data['bookid'])
        thisauther = showauther(data['autherinfo'])
        thisbook.authers.add(thisauther)
    return redirect('/books/'+str(data['bookid']))


def show_all_authers(request):
    context = {
        'all_authers': allauthers()
    }
    return render(request, 'AhowAuthers.html', context)


def create_auther(request):
    if request.method == 'POST':
        data = request.POST
        createauther(data)
    return redirect('/authers/')


def add_book_to_auther(request):
    if request.method == 'POST':
        dataauther = request.POST
        addbooktoauther(dataauther['autherid'], dataauther['bookinfo'])
    return redirect('/authers/'+str(dataauther['autherid']))


def show_auther(request, id):
    context = {'auther': showauther(id),
               'books': autherbooks(id).values(),
               'allbooks': allbooks()
               }
    print('alaa'*30)
    print(context['books'])
    return render(request, 'ShowAuther.html', context)
