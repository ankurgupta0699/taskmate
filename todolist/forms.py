from django import forms

from todolist.models import TaskModel


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['task', 'done']
