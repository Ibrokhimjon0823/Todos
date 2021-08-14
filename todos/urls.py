from django.urls import path
from .views import TodoListCreate, TodoCompleteSerializer

urlpatterns = [
    path('<int:pk>/', TodoCompleteSerializer.as_view()),
    path('', TodoListCreate.as_view()),
]