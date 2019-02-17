import django_filters
from rest_framework import viewsets, filters

from django.shortcuts import render

from .models import Task
from .serializer import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer
