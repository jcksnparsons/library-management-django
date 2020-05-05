import sqlite3
from django.shortcuts import render
from libraryapp.models import Library, model_factory
from ..connection import Connection
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect

@login_required
def list_libraries(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Library)
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                l.id,
                l.name,
                l.address
            from libraryapp_library l
            """)

            all_libraries = db_cursor.fetchall()

        template = 'libraries/list.html'
        context = {
            'all_libraries': all_libraries
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO libraryapp_library
            (
                name, address
            )
            VALUES (?, ?)
            """,
            (form_data['name'], form_data['address']))

        return redirect(reverse('libraryapp:libraries'))