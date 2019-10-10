from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    """The author of poems"""
    name_en = models.CharField(max_length=100)
    name_zh = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        """Return a string representation of the model"""
        return self.name_en + ', ' + self.name_zh


class Poem(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text[:100] + '...'


class Translation(models.Model):
    poem = models.ForeignKey(Poem, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    translator = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.text[:100] + '...'



class Question(models.Model):
    poem = models.ForeignKey(Poem, on_delete=models.PROTECT)
    question = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    answer = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

