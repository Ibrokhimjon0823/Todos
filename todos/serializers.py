from django.db.models import fields
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'body')

class TodoCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','title','body']
        # read_only_fields = ['title','body']