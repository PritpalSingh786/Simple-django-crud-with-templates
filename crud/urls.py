from django.urls import path
from .views import getAllTodos, addTodo, updateTodo, deleteTodo

urlpatterns = [
    path('', getAllTodos, name='getAllTodos'),
    path('addTodo/', addTodo, name='addTodo'),
    path('updateTodo/<int:id>/', updateTodo, name='updateTodo'),
    path('deleteTodo/<int:id>/', deleteTodo, name='deleteTodo'),
    
]