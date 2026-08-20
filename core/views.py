from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST

from .models import Task, Tag
from .forms import TaskForm, TagForm


class TaskListView(generic.ListView):
    model = Task
    template_name = "core/task_list.html"
    context_object_name = "tasks"
    ordering = ["is_completed"]


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = "core/task_detail.html"
    context_object_name = "task"


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "core/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("core:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "core/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("core:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("core:task-list")
    template_name = "core/task_confirm_delete.html"


class TagListView(generic.ListView):
    model = Tag
    template_name = "core/tag_list.html"
    context_object_name = "tags"


class TagUpdateView(generic.UpdateView):
    model = Tag
    template_name = "core/tag_form.html"
    form_class = TagForm
    success_url = reverse_lazy("core:tag-list")


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = "core/tag_form.html"
    form_class = TagForm
    success_url = reverse_lazy("core:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "core/tag_confirm_delete.html"
    success_url = reverse_lazy("core:tag-list")


@require_POST
def toggle_complete_button(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect("core:task-list")
