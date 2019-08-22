from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    pass


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, null=True, on_delete=models.CASCADE)
