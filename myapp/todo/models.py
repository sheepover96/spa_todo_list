from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
  pass

class Task(models.Model):
  name = models.CharField(max_length=100)

  def __str___(self):
    return self.name