from django import forms
from .models import Author, Poem, Question, Answer

LANGUAGES = (
    (1, '英语'),
    (2, '法语'),
    (3, '日语'),
    (4, '西班牙语'),
    (5, '德语'),
    (6, '俄语'),
)
CATEGORIES = [
    (1, '翻译'),
    (2, '问答'),
    (3, '批评'),
    (4, '分解'),
]


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'name_zh', 'language', 'born', 'died', 'detail']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '外文名',
                                              'class': 'form-control'}),
            'name_zh': forms.TextInput(attrs={'placeholder': '中文名',
                                              'class': 'form-control'}),
            'language': forms.Select(attrs={'class': 'form-control'},
                                     choices=LANGUAGES),
            'born': forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd',
                'class': 'form-control'}),
            'died': forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}),
            'detail': forms.Textarea(attrs={'class': 'form-control'}),
        }


class PoemForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={ 'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['category', 'title', 'author', 'text']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'},
                                     choices=CATEGORIES),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']
        widgets = {
            'answer': forms.Textarea(attrs={'class': 'form-control'}),
        }

