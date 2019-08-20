"""Defines URL patterns for poems"""

from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Show all authors
    path('authors/', views.authors, name='authors'),

    # Detail page for a single author
    path('authors/<int:author_id>/', views.author, name='author'),

    # Show poem
    path('authors/<int:author_id>/<int:poem_id>/', views.poem, name='poem'),

    # Page for adding a new author
    path('new_author/', views.new_author, name='new_author'),

    # Page for adding a new poem
    path('new_poem/<int:author_id>/', views.new_poem, name='new_poem'),

    # Page for editing a poem
    path('edit_poem/<int:poem_id>/', views.edit_poem, name='edit_poem')
]