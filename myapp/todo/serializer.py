from rest_framework import serializers
from .models import MyUser, Task

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = ('id','name',)