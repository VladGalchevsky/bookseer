from typing import Any
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, CreateView
from django.forms import widgets

from books.models import Books
from books.forms import BooksForm

from PIL import Image


def books_list(request):
    books = Books.objects.all()
    # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('name', 'format', 'root'):
        books = books.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            books = books.reverse()
            
    # paginate books
    paginator = Paginator(books, 5)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        books = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver
    # last page of results.
        books = paginator.page(paginator.num_pages)
    
    return render(request, 'books/books_list.html', {'books': books})


class BooksAddView(CreateView):
    model = Books
    form_class = BooksForm
    template_name = 'books/books_add.html'
    success_url = reverse_lazy('books_list')

    def form_valid(self, form):
        # Custom validation and saving logic
        errors = {}

        if form.is_valid():
            # Perform additional form validation
            photo = form.cleaned_data.get('photo')
            if photo:
                if photo.size > 2 * 1024 * 1024:
                    errors['photo'] = 'Фото повинно бути не більше 2 МБ'
                else:
                    try:
                        img = Image.open(photo)
                        img.verify()
                    except:
                        errors['photo'] = 'Неприпустимий формат зображення'

        if errors:
            # Render the template with errors
            return self.render_to_response(self.get_context_data(form=form, errors=errors))

        # Save the form and display success message
        response = super().form_valid(form)
        messages.success(self.request, 'Книгу успішно додано!')
        return response

    def form_invalid(self, form):
        # Render the template with form errors
        return self.render_to_response(self.get_context_data(form=form))
        
    def get_success_url(self) -> str:
        return f"{reverse('books_list')}?status_message=Книгу успішно збережено!"
    
    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.success(request, 'Додавання книги скасовано!')
            return redirect('books_list')
        else:
            return super().post(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context variables if needed
        return context


class BooksUpdateView(UpdateView):
    model = Books
    fields = '__all__'
    template_name = 'books/books_edit.html'

    def get_success_url(self) -> str:
        return f"{reverse('books_list')}?status_message=Книгу успішно збережено!"
    
    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                f"{reverse('books_list')}?status_message=Книгу успішно збережено!")
        else:
            return super().post(request, *args, **kwargs)