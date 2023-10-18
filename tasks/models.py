from django.db import models
from django.contrib.auth.models import User


class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)
    isComplete = models.BooleanField(default=False)
    deadLine = models.DateTimeField()

    def __str__(self):
        return self.title


class subTasks(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE, related_name='subtasks', null=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)
    isComplete = models.BooleanField(default=False)
    deadLine = models.DateTimeField()
    def __str__(self):
        return self.title
