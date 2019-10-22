"""Defines URL patterns for poems"""

from django.urls import path, re_path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # 导航栏页面tabs
    path('authors/', views.authors, name='authors'),
    path('authors/<int:author_id>/', views.author, name='author'),
    path('questions/', views.questions, name='questions'),
    path('translations/', views.translations, name='translations'),

    # 诗歌页面tabs
    path('poems/<int:poem_id>/', views.poem, name='poem'),  # 空白
    path('poems/<int:poem_id>/translations/<int:translation_id>/', views.poem_translation, name='poem_translation'),  # 译文
    path('poems/<int:poem_id>/questions/', views.poem_questions, name='poem_questions'),  # 问
    path('poems/<int:poem_id>/questions/<int:question_id>/', views.poem_question, name='poem_question'),  # 答案详情页
    path('poems/<int:poem_id>/critics/', views.poem_critics, name='poem_critics'),  # 批评
    path('poems/<int:poem_id>/critics/<int:critic_id>/', views.poem_critic, name='poem_critic'),  # 批评
    # path('poems/<int:poem_id>/<int:tabnum>/', views.poem, name='poem'),  # 分解
    # path('poems/<int:poem_id>/<int:tabnum>/', views.poem, name='poem'),  # 查词

    # 新增
    path('new_author/', views.new_author, name='new_author'),
    path('new_poem/<int:author_id>/', views.new_poem, name='new_poem'),
    path('new_translation/<int:poem_id>/', views.new_translation, name='new_translation'),
    path('new_question/<int:poem_id>/', views.new_question, name='new_question'),
    path('new_answer/<int:question_id>/', views.new_answer, name='new_answer'),

    # 修改
    path('edit_author/<int:author_id>/', views.edit_author, name='edit_author'),
    path('edit_poem/<int:poem_id>/', views.edit_poem, name='edit_poem'),
    path('edit_translation/<int:translation_id>/', views.edit_translation, name='edit_translation'),
]
