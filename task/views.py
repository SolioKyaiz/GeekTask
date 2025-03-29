from django.shortcuts import render
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer
from rest_framework import generics, status, permissions


class TaskListAPIView(generics.ListAPIView):  # Список
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskCreateAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailAPIView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class =  TaskSerializer

class TaskUpdateAPIView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class =  TaskSerializer

class TaskDeleteAPIView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


