import sqlite3
from django.shortcuts import render
from libraryapp.models import Book, Librarian, Library
from ..connection import Connection
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect

@login_required
def book_list(request):
    if request.method == 'GET':
        all_books = Book.objects.all()
       
        template = 'books/list.html'
        context = {
            'all_books': all_books
        }

        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST

        new_book = Book()
        new_book.title = form_data['title']
        new_book.author = form_data['author']
        new_book.ISBN_num = form_data['ISBN_num']
        new_book.year_published = form_data['year_published']

        librarian = Librarian()
        librarian.id = request.user.librarian.id
        new_book.librarian = librarian

        library = Library()
        library.id = form_data['location']
        new_book.location = library

        new_book.save()

        return redirect(reverse('libraryapp:books'))