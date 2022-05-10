from todolist import views
from django.urls import path

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('edit/<task_id>', views.edit_task, name='edit_task'),
    path('toggle_task_status/<task_id>', views.toggle_task_status, name='toggle_task_status'),
]
