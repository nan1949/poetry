from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Author, Poem, Translation
from .forms import AuthorForm, PoemForm, TranslationForm


# Create your views here.
def index(request):
    """The home page for Poetry"""
    return render(request, 'poems/index.html')


def authors(request):
    """Show all authors"""
    authors = Author.objects.order_by('date_added')
    context = {'authors': authors}
    return render(request, 'poems/authors.html', context)


def author(request, author_id):
    """Show a single author and all its poems."""
    author = Author.objects.get(id=author_id)
    poems = author.poem_set.order_by('-date_added')
    context = {'author': author, 'poems': poems}
    return render(request, 'poems/author.html', context)


def poem(request, author_id, poem_id):
    """Show poem"""
    author = Author.objects.get(id=author_id)
    poem = Poem.objects.get(id=poem_id)
    translations = poem.translation_set.order_by('-date_added')
    context = {'author': author, 'poem': poem, 'translations': translations}
    return render(request, 'poems/poem.html', context)


@login_required
def new_author(request):
    """Add a new author"""
    if request.method != 'POST':
        # No data submitted; blank form
        form = AuthorForm()
    else:
        # POST data submitted; process data.
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_author = form.save(commit=False)
            new_author.owner = request.user
            new_author.save()
            return HttpResponseRedirect(reverse('authors'))

    context = {'form': form}
    return render(request, 'poems/new_author.html', context)


@login_required
def new_poem(request, author_id):
    """Add a new poem for a particular author"""
    author = Author.objects.get(id=author_id)

    if request.method != 'POST':
        form = PoemForm()
    else:
        form = PoemForm(data=request.POST)
        if form.is_valid():
            new_poem = form.save(commit=False)
            new_poem.author = author
            new_poem.owner = request.user
            new_poem.save()
        return HttpResponseRedirect(reverse('author', args=[author_id]))

    context = {'author': author, 'form': form}
    return render(request, 'poems/new_poem.html', context)


@login_required
def new_translation(request, author_id, poem_id):
    author = Author.objects.get(id=author_id)
    poem = Poem.objects.get(id=poem_id)
    if request.method != 'POST':
        form = TranslationForm()
    else:
        form = TranslationForm(data=request.POST)
        if form.is_valid():
            new_translation = form.save(commit=False)
            new_translation.poem = poem
            new_translation.owner = request.user
            new_translation.save()
        return HttpResponseRedirect(reverse('poem', args=[author_id, poem_id]))

    context = {'author': author, 'poem': poem, 'form': form}
    return render(request, 'poems/new_translation.html', context)


@login_required
def edit_poem(request, poem_id):
    """Edit an existing poem"""
    poem = Poem.objects.get(id=poem_id)
    author = poem.author
    if poem.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current poem.
        form = PoemForm(instance=poem)
    else:
        form = PoemForm(instance=poem, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('author', args=[author.id]))

    context = {'poem': poem, 'author': author, 'form': form}
    return render(request, 'poems/edit_poem.html', context)
