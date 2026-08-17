from django.views import generic
from django.shortcuts import render
from .models import Task, Tag


class TaskListView(generic.ListView):
    class Meta:
        model = Task
        fields = ["content", "datetime", "deadline_datetime", "is_completed", "tags"]
        template_name = "templates/tasks_list.html"
        context_object_name = "tasks"
        ordering = ["-created_at"]