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

from books.views import (
    books_list,
    books_add,
    books_edit,
    books_delete,
    contact_admin,
)

urlpatterns = [
    path('', books_list, name='books_list'),
    path('books/add/', books_add, name='books_add'),
    path('books/<int:sid>/edit/', books_edit, name='books_edit'),
    path('books/<int:sid>/delete/', books_delete, name='books_delete'),
    path('contact-admin/', contact_admin, name='contact_admin'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
