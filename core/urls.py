from django.urls import path
from .views import (
    TaskListView,
    TaskDetailView,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    toggle_complete_button,
    TagUpdateView,
    TagCreateView,
    TagDeleteView,
    TaskDeleteView,
)

app_name = "core"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tag-list/", TagListView.as_view(), name="tag-list"),
    path("task/<int:pk>/toggle/", toggle_complete_button, name="task-toggle"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]
