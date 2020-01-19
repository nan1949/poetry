from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Author, Poem, Question, Answer, Translation
from .forms import AuthorForm, PoemForm, QuestionForm, AnswerForm, TranslationForm


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


def poem(request, poem_id):
    poem = Poem.objects.get(id=poem_id)
    author = poem.author
    questions = poem.question_set.order_by('-date_added')
    context = {'author': author, 'poem': poem,
               'questions': questions}
    return render(request, 'poems/poem.html', context)


def translations(request):
    translations = Translation.objects.all()
    context = {'translations': translations}
    return render(request, 'poems/translations.html', context)


def poem_translations(request, poem_id):
    poem = Poem.objects.get(id=poem_id)
    author = poem.author
    translations = poem.translation_set.order_by('-date_added')
    context = {'author': author, 'poem': poem, 'translations': translations, }
    return render(request, 'poems/poem_translations.html', context)


def poem_translation(request, translation_id):
    translation = Translation.objects.get(id=translation_id)
    poem = translation.poem
    author = poem.author
    context = {'author': author, 'poem': poem, 'translation': translation}
    return render(request, 'poems/poem_translation.html', context)


def poem_questions(request, poem_id):
    poem = Poem.objects.get(id=poem_id)
    author = poem.author
    questions = poem.question_set.order_by('-date_added')
    context = {'author': author, 'poem': poem,
               'questions': questions}
    return render(request, 'poems/poem_questions.html', context)


def poem_question(request, question_id):
    question = Question.objects.get(id=question_id)
    poem = question.poem
    author = poem.author
    context = {'author': author, 'poem': poem, 'question': question}
    return render(request, 'poems/poem_question.html', context)


def questions(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'poems/questions.html', context)


def poem_critics(request, poem_id):
    poem = Poem.objects.get(id=poem_id)
    translations = poem.translation_set
    author = poem.author
    critics = poem.critic_set.order_by('-date_added')
    context = {'author': author, 'poem': poem,
               'critics': critics, 'translations': translations}
    return render(request, 'poems/poem_critics.html', context)


def poem_critic(request, poem_id, critic_id):
    poem = Poem.objects.get(id=poem_id)
    translations = poem.translation_set
    author = poem.author
    critic = Critic.objects.get(id=critic_id)
    context = {'author': author, 'poem': poem,
               'critic': critic, 'translations': translations}
    return render(request, 'poems/poem_critic.html', context)


@login_required
def new_author(request):
    if request.method != 'POST':
        form = AuthorForm()
    else:
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
def new_translation(request, poem_id):
    poem = Poem.objects.get(id=poem_id)
    author = poem.author
    if request.method != 'POST':
        form = TranslationForm()
    else:
        form = TranslationForm(data=request.POST)
        if form.is_valid():
            new_translation = form.save(commit=False)
            new_translation.poem = poem
            new_translation.owner = request.user
            new_translation.save()
        return HttpResponseRedirect(reverse('poem', args=[author.id, poem_id]))

    context = {'author': author, 'poem': poem, 'form': form}
    return render(request, 'poems/new_translation.html', context)


@login_required
def new_question(request, poem_id):
    poem = Poem.objects.get(id=poem_id)
    author = poem.author
    if request.method != 'POST':
        form = QuestionForm()
    else:
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            new_question = form.save(commit=False)
            new_question.poem = poem
            new_question.owner = request.user
            new_question.save()
        return HttpResponseRedirect(reverse('poem', args=[poem.id]))
    context = {'author': author, 'poem': poem, 'form': form}
    return render(request, 'poems/new_question.html', context)


@login_required
def new_answer(request, question_id):
    question = Question.objects.get(id=question_id)
    poem = question.poem
    author = poem.author
    if request.method != 'POST':
        form = AnswerForm()
    else:
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            new_answer = form.save(commit=False)
            new_answer.question = question
            new_answer.owner = request.user
            new_answer.save()
        return HttpResponseRedirect(reverse('poem_question', args=[question.id]))
    context = {'author': author, 'poem': poem, 'question': question, 'form': form}
    return render(request, 'poems/new_answer.html', context)


@login_required
def edit_poem(request, poem_id):
    poem = Poem.objects.get(id=poem_id)
    author = poem.author
    if poem.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = PoemForm(instance=poem)
    else:
        form = PoemForm(instance=poem, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('poem', args=[poem.id]))

    context = {'poem': poem, 'author': author, 'form': form}
    return render(request, 'poems/edit_poem.html', context)

@login_required
def edit_translation(request, translation_id):
    translation = Translation.objects.get(id=translation_id)
    poem = translation.poem
    author = poem.author
    if translation.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = TranslationForm(instance=translation)
    else:
        form = TranslationForm(instance=translation, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('poem', args=[poem.id]))
    context = {'translation': translation, 'poem': poem, 'author': author, 'form': form}
    return render(request, 'poems/edit_translation.html', context)


@login_required
def edit_author(request, author_id):
    author = Author.objects.get(id=author_id)
    if author.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = AuthorForm(instance=author)
    else:
        form = AuthorForm(instance=author, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('author', args=[author_id]))
    context = {'author': author, 'form': form}
    return render(request, 'poems/edit_author.html', context)


@login_required
def delete_answer(request, answer_id):
    answer = Answer.objects.get(id=answer_id)
    question = answer.question
    if request.method == 'POST':
        if answer.owner != request.user:
            raise Http404
        answer.delete()
        return HttpResponseRedirect(reverse('poem_question', args=[question.id]))
    context = {'answer': answer}
    return render(request, 'poems/delete_answer.html', context)