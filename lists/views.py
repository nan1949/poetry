from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item


def lists_home(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/lists/')

    items = Item.objects.all()
    return render(request, 'lists/lists_home.html', {'items': items})
