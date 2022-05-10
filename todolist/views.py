from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from todolist import models as todolist_models
from todolist.forms import TaskForm


def index(request):
    context = {
        'index_text': 'Welcome to Taskmate!',
    }
    return render(request, 'index.html', context)

@login_required
def todolist(request):
    if request.method=='POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            messages.success(request, 'New Task Added!')
        return redirect('todolist')
    else:
        all_tasks = todolist_models.TaskModel.objects.filter(owner=request.user)
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        context = {
            'all_tasks': all_tasks,
        }
        return render(request, 'todolist.html', context)

@login_required
def delete_task(request, task_id):
    task_obj = todolist_models.TaskModel.objects.get(pk=task_id)
    if task_obj.owner == request.user:
        task_obj.delete()
    else:
        messages.error(request, 'Access Denied! Action not allowed!')

    return redirect('todolist')

@login_required
def edit_task(request, task_id):    
    task_obj = todolist_models.TaskModel.objects.get(pk=task_id)
    if task_obj.owner == request.user:
        if request.method=='POST':
            form = TaskForm(request.POST or None, instance=task_obj)
            if form.is_valid():
                form.save()
                messages.success(request, 'Task Updated!')
            return redirect('todolist')
        else:
            context = {
                'task_obj': task_obj,
            }
            return render(request, 'edit.html', context)
    else:
        messages.error(request, 'Access Denied! Action not allowed!')

    return redirect('todolist')

@login_required
def toggle_task_status(request, task_id):
    task_obj = todolist_models.TaskModel.objects.get(pk=task_id)
    if task_obj.owner == request.user:
        task_obj.done = not task_obj.done
        task_obj.save()
    else:
        messages.error(request, 'Access Denied! Action not allowed!')

    return redirect('todolist')


def contact(request):
    context = {
        'contact_text' : 'Contact from Jinja2.',
    }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'about_text': 'About from Jinja2.',
    }
    return render(request, 'about.html', context)
