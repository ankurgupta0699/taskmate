from django.contrib import admin

from todolist import models as todolist_models


admin.site.register(todolist_models.TaskModel)
