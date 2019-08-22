"""Defines URL patterns for lists"""

from django.urls import path
from . import views

urlpatterns = [
    #
    path('', views.lists_home, name='lists_home'),
]