from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

def getAllTodos(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {
        "todos":todos
    })

def addTodo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Todo.objects.create(title=title, description=description)
        return redirect('getAllTodos')
    return render(request, 'Add_Update.html', {
        "action":"Add",
    })

def updateTodo(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
        return redirect('getAllTodos')
    return render(request, 'Add_Update.html', {
        "action":"Update", "todo":todo
    })

def deleteTodo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('getAllTodos')
