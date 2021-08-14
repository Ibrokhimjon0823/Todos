from django.db import models
from django.shortcuts import render
from rest_framework import generics, serializers
from .models import Todo
from .serializers import TodoSerializer,TodoCompleteSerializer

class TodoListCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoCompleteSerializer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoCompleteSerializer   