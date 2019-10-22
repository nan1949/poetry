from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name_en = models.CharField(max_length=100)
    name_zh = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    born = models.DateField(null=True)
    died = models.DateField(null=True)
    detail = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_en + ', ' + self.name_zh


class Poem(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)


class Translation(models.Model):
    poem = models.ForeignKey(Poem, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    translator = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)


class Question(models.Model):
    category = models.CharField(max_length=200)  # 翻译、问答、批评、分解放在同一个model中
    poem = models.ForeignKey(Poem, on_delete=models.PROTECT)
    title = models.TextField()
    text = models.TextField()
    author = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    answer = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)


class Critic(models.Model):
    poem = models.ForeignKey(Poem, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
