"""books_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from books.views.contact_admin import ContactAdminView
from books.views.books import (
    books_list,
    BooksAddView,
    BooksUpdateView,
)


urlpatterns = [
    path('', books_list, name='books_list'),
    path('books/add/', BooksAddView.as_view(), name='books_add'),
    path('books/<int:pk>/edit/', BooksUpdateView.as_view(), name='books_edit'),
    path('contact-admin/', ContactAdminView.as_view(), name='contact_admin'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
