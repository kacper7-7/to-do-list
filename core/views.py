from django.views import generic
from .models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "core/task_list.html"
    context_object_name = "tasks"
    ordering = ["-is_completed"]


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = "core/task_detail.html"
    context_object_name = "task"
