from django.db import models
from django.contrib.auth.models import User


class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    time = models.DateTimeField()
    isComplete = models.BooleanField(default=False)
    deadLine = models.DateTimeField()


class subTasks(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    time = models.DateTimeField()
    isComplete = models.BooleanField(default=False)
    deadLine = models.DateTimeField()
