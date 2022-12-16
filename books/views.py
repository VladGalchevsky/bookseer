from django.http import HttpResponse
from django.shortcuts import render


def books_list(request):
    return render(request, 'books/books_list.html', {})


def books_add(request):
    return HttpResponse('<h1>books add form</h1>')


def books_edit(request, sid):
    return HttpResponse(f'<h1>edit books {sid}</h1>')


def books_delete(request, sid):
    return HttpResponse(f'<h1>delete  {sid}</h1>')
