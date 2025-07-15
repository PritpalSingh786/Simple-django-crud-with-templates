from django.shortcuts import render, redirect
from .models import Todo
import os 

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
        "action":os.getenv('Add'),
    })

def updateTodo(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
        return redirect('getAllTodos')
    return render(request, 'Add_Update.html', {
        "action":os.getenv('Update'), "todo":todo
    })

def deleteTodo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('getAllTodos')

# Class based views

# from django.views import View
# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Todo
# import os

# # GET all todos
# class TodoListView(View):
#     def get(self, request):
#         todos = Todo.objects.all()
#         return render(request, 'index.html', {
#             "todos": todos
#         })


# # Create a new todo
# class TodoCreateView(View):
#     def get(self, request):
#         return render(request, 'Add_Update.html', {
#             "action": os.getenv('Add')
#         })

#     def post(self, request):
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         Todo.objects.create(title=title, description=description)
#         return redirect('getAllTodos')


# # Update existing todo
# class TodoUpdateView(View):
#     def get(self, request, id):
#         todo = get_object_or_404(Todo, id=id)
#         return render(request, 'Add_Update.html', {
#             "action": os.getenv('Update'),
#             "todo": todo
#         })

#     def post(self, request, id):
#         todo = get_object_or_404(Todo, id=id)
#         todo.title = request.POST.get('title')
#         todo.description = request.POST.get('description')
#         todo.save()
#         return redirect('getAllTodos')


# # Delete a todo
# class TodoDeleteView(View):
#     def get(self, request, id):
#         todo = get_object_or_404(Todo, id=id)
#         todo.delete()
#         return redirect('getAllTodos')

