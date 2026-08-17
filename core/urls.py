from django.urls import path
from .views import TaskListView, TaskDetailView, TagListView, TaskCreateView, TaskUpdateView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("tag-list/", TagListView.as_view(), name="tag-list"),
]


app_name = "tasks"