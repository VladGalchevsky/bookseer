from django.contrib import admin
from django.urls import reverse

from .models import Books


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'format', 'root', 'bookmark', 'captal', 'photo']
    list_display_links = ['name']
    list_editable = ['root']
    ordering = ['name']
    list_filter = ['format', 'root']
    list_per_page = 10
    search_fields = ['name', 'format', 'root']
    
    def view_on_site(self, obj):
        return reverse('books_edit', kwargs={'pk': obj.id})

admin.site.register(Books, BookAdmin)
