from django.db import models
from django.contrib.auth.models import User


class TaskModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=500)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task + " " + str(self.done)