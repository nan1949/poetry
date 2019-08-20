from django import forms
from .models import Author, Poem


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name_en', 'name_zh']
        labels = {'name_en': '', 'name_zh': ''}


class PoemForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = ['title', 'text']
        labels = {'title': '', 'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
