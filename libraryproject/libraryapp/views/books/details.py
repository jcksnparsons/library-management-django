import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book, Library, Librarian
from libraryapp.models import model_factory
from ..connection import Connection

def get_book(book_id):
    return Book.objects.get(pk=book_id)

@login_required
def book_details(request, book_id):
    if request.method == 'GET':
        book = get_book(book_id)
        template_name = 'books/detail.html'
        return render(request, template_name, {'book': book})

    elif request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for editing a book
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            book = Book.objects.get(pk=book_id)
            book.title = form_data['title']
            book.author = form_data['author']
            book.ISBN_num = form_data['ISBN_num']
            book.year_published = form_data['year_published']

            library = Library()
            library.id = form_data['location'] 
            book.location = library

            book.save()

            return redirect(reverse('libraryapp:books'))

        # Check if this POST is for deleting a book
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            book = Book.objects.get(pk=book_id)
            book.delete()
            
            return redirect(reverse('libraryapp:books'))

    