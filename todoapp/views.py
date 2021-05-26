from django.shortcuts import redirect, render, get_object_or_404
from todoapp.models import Category, TodoList
from .forms import CreateTask


def index(request):
    todos = TodoList.objects.all()
    return render(request, "todoapp/todo.html", {'todos': todos})


def create_task(request):
    query_results = Category.objects.all()
    if request.method == "POST":
        form = CreateTask(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CreateTask()
    return render(request, "todoapp/create.html", {"form": form, "category": query_results})


def task_detail(request, pk):
    task = get_object_or_404(TodoList, pk=pk)
    return render(request, "todoapp/detail.html", {'task': task})


def edit_task(request, pk):
    task = get_object_or_404(TodoList, pk=pk)
    if request.method == "POST":
        form = CreateTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("detail")
    else:
        form = CreateTask(instance=task)
    return render(request, "todoapp/edit.html", {"form": form})


def delete_task(request, pk):
    task = get_object_or_404(TodoList, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("index")
    return render(request, "todoapp/delete.html", {'task': task})
