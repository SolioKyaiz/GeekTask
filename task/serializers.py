from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title','description','completed','created')

