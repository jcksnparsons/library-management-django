import sqlite3
from django.shortcuts import render
from libraryapp.models import Library, Book
from ..connection import Connection
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect

@login_required
def list_libraries(request):
    if request.method == 'GET':
        all_libraries = Library.objects.all()
        
        for library in all_libraries:
            library.books = Book.objects.filter(location_id = library.id)
        
        template = 'libraries/list.html'
        context = {
            'all_libraries': all_libraries
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        new_library = Library()
        new_library.name = form_data['name']
        new_library.address = form_data['address']

        new_library.save()

        return redirect(reverse('libraryapp:libraries'))