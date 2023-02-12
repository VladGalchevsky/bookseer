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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from allauth.socialaccount.providers.google import views as google_views

from books.views.contact_admin import ContactAdminView
from books.views.books import (
    books_list,
    BooksAddView,
    BooksUpdateView,
    BooksDeleteView,
)


urlpatterns = [
    path('accounts/profile/', login_required(TemplateView.as_view(
        template_name='account/profile.html')), name='profile'),
    path('accounts/', include('allauth.urls')),
    path('accounts/google/login/', google_views.oauth2_login, name='google_login'),
    path('accounts/google/callback/', google_views.oauth2_callback, name='google_callback'),
    path('', books_list, name='books_list'),
    path('books/add/', BooksAddView.as_view(), name='books_add'),
    path('books/<int:pk>/edit/', BooksUpdateView.as_view(), name='books_edit'),
    path('books/<int:pk>/delete/', BooksDeleteView.as_view(),
         name='books_delete'),
    path('contact-admin/', ContactAdminView.as_view(), name='contact_admin'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
