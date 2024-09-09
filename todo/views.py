from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import ToDoForm
from .models import Todo


# Create your views here.

def home(request):
    return render(request, 'todo/home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodo')
            except IntegrityError:
                render(request, 'todo/signupuser.html',
                       {'form': UserCreationForm(), 'error': "That username already been taken"})
        else:
            return render(request, 'todo/signupuser.html',
                          {'form': UserCreationForm(), 'error': "Password didn't match"})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})

    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/loginuser.html', {'form': AuthenticationForm(), 'error': "User doesn't exist"})
        else:
            login(request, user)
            return redirect('currenttodo')


@login_required
def currenttodo(request):
    todos = Todo.objects.filter(user=request.user, time_done__isnull=True)
    return render(request, 'todo/currenttodo.html', {'todos': todos})


@login_required
def todoread(request, todo_pk):
    read = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    form_correct = ToDoForm(instance=read)
    if request.method == "POST":
        try:
            form = ToDoForm(request.POST, instance=read)
            form.save()
            return redirect('currenttodo')
        except ValueError:
            return render(request, 'todo/todoread.html',
                          {"list_todos": read, 'correct': form_correct, 'error': 'Введены неверные данные'})

    return render(request, 'todo/todoread.html', {"list_todos": read, 'correct': form_correct})


@login_required
def complete_tasks(request):
    todos = Todo.objects.filter(user=request.user, time_done__isnull=False).order_by('-time_done')
    return render(request, 'todo/complete_tasks.html', {'todos': todos})


@login_required
def tododone(request, todo_pk):
    read_task = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == "POST":
        read_task.time_done = timezone.now()
        read_task.save()
        return redirect('currenttodo')


@login_required
def tododelete(request, todo_pk):
    read_task = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == "POST":
        read_task.delete()
        return redirect('currenttodo')


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

@login_required
def todocreate(request):
    if request.method == 'GET':
        return render(request, 'todo/todocreate.html', {'form': ToDoForm()})
    else:
        try:
            form = ToDoForm(request.POST)
            if form.is_valid():
                new_todo = form.save(commit=False)
                new_todo.user = request.user
                new_todo.save()
                return redirect('currenttodo')
            else:
                return (request, 'todo/todocreate.html', {'form': form})
        except ValueError:
            return render(request, 'todo/todocreate.html', {'form': ToDoForm(), 'error': 'Wrong data input'})
