from django import forms
from .models import Author, Poem, Translation, Question, Answer


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name_en', 'name_zh']
        widgets = {
            'name_en': forms.TextInput(attrs={'placeholder': '诗人原名'}),
            'name_zh': forms.TextInput(attrs={'placeholder': '诗人中文名'})
        }


class PoemForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '原诗标题', }),
            'text': forms.Textarea(attrs={'cols': 80, 'placeholder': '原诗内容', }),
        }


class TranslationForm(forms.ModelForm):
    class Meta:
        model = Translation
        fields = ['title', 'translator', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '译诗标题', }),
            'translator': forms.TextInput(attrs={'placeholder': '译者名字'}),
            'text': forms.Textarea(attrs={'cols': 80, 'placeholder': '译诗内容', })
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question']
        widgets = {
            'question': forms.Textarea(attrs={'cols': 80, 'placeholder': '问题'}),
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']
        widgets = {
            'answer': forms.Textarea(attrs={'cols': 80, 'placeholder': '回答'}),
        }
