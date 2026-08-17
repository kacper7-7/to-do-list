from django.views import generic
from django.urls import reverse_lazy
from .models import Task, Tag
from .forms import TaskForm


class TaskListView(generic.ListView):
    model = Task
    template_name = "core/task_list.html"
    context_object_name = "tasks"
    ordering = ["is_completed"]


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = "core/task_detail.html"
    context_object_name = "task"


class TaskCreateView(generic.UpdateView):
    model = Task
    template_name = "core/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")

class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "core/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class TagListView(generic.ListView):
    model = Tag
    template_name = "core/tag_list.html"
    context_object_name = "tags"

