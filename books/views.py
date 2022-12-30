from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from books.models import Books


def books_list(request):
    books = Books.objects.all()
    # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('name', 'format', 'root'):
        books = books.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            books = books.reverse()
    return render(request, 'books/books_list.html', {'books': books})


def books_add(request):
    if request.method == "POST":
        if request.POST.get('add_button') is not None:
            # TODO: validate input from user
            errors = {}
            if not errors:
                books = Books(
                    name=request.POST['name'],
                    format=request.POST['format'],
                    root=request.POST['root'],
                    bookmark=request.POST['bookmark'],
                    captal=request.POST['captal'],
                    photo=request.FILES.get('photo'),
                )
                books.save()
                return HttpResponseRedirect(reverse('books_list'))
            else:
                return render(request, 'books/books_add.html', {})
        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            return HttpResponseRedirect(reverse('books_list'))
    else:
        return render(request, 'books/books_add.html', {})


def books_edit(request, sid):
    return HttpResponse(f'<h1>edit books {sid}</h1>')


def books_delete(request, sid):
    return HttpResponse(f'<h1>delete  {sid}</h1>')


def contact_admin(request):
    return render(request, 'contact_admin/form.html', {})


def color_view(request):
    if request.method == 'POST':
        bookmark = request.POST.get('bookmark')
        captal = request.POST.get('captal')
        color_model = Books(bookmark=bookmark, captal=captal)
        color_model.save()
    return render(request, 'books_list.html', {'color_model': color_model})
