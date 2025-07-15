from django.urls import path
from .views import getAllTodos, addTodo, updateTodo, deleteTodo

urlpatterns = [
    path('', getAllTodos, name='getAllTodos'),
    path('addTodo/', addTodo, name='addTodo'),
    path('updateTodo/<int:id>/', updateTodo, name='updateTodo'),
    path('deleteTodo/<int:id>/', deleteTodo, name='deleteTodo'),
    
]


# from django.urls import path
# from .views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView

# urlpatterns = [
#     path('', TodoListView.as_view(), name='getAllTodos'),
#     path('add/', TodoCreateView.as_view(), name='addTodo'),
#     path('update/<int:id>/', TodoUpdateView.as_view(), name='updateTodo'),
#     path('delete/<int:id>/', TodoDeleteView.as_view(), name='deleteTodo'),
# ]
