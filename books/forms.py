from django import forms
from .models import Books


class BooksForm(forms.ModelForm):
    bookmark = forms.CharField(required=False, 
                               widget=forms.TextInput(attrs={'type': 'color'}))
    captal = forms.CharField(required=False, 
                             widget=forms.TextInput(attrs={'type': 'color'}))

    class Meta:
        model = Books
        fields = ['name', 'format', 'root', 'bookmark', 'captal', 'photo']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.initial['bookmark'] = instance.bookmark
            self.initial['captal'] = instance.captal
        else:
            self.initial['bookmark'] = '#FFFFFF'  # Встановлюємо білий колір за замовчуванням
            self.initial['captal'] = '#FFFFFF'  # Встановлюємо білий колір за замовчуванням