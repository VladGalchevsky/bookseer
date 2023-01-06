from django import forms
from .models import Books
from colorfield.widgets import ColorWidget

from colorful.forms import RGBColorField

class BooksForm(forms.ModelForm):
    bookmark = RGBColorField(required=False, widget=ColorWidget)
    captal = RGBColorField(required=False, widget=ColorWidget)

    class Meta:
        model = Books
        fields = ['name', 'format', 'root', 'bookmark', 'captal', 'photo']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['bookmark'] = '#FFFFFF'  # Встановлюємо білий колір за замовчуванням
        self.initial['captal'] = '#FFFFFF'  # Встановлюємо білий колір за замовчуванням