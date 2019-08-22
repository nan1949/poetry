from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from lists.models import Item, List
from django.urls import reverse


def lists_home(request):
    return render(request, 'lists/lists_home.html')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'lists/list.html', {'list': list_})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return HttpResponseRedirect(reverse('view_list', args=[list_.id]))


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return HttpResponseRedirect(reverse('view_list', args=[list_.id]))
