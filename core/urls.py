from django.urls import path
from .views import TaskListView, TaskDetailView, TagListView, TagDetailView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task-detail/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tag-list/", TagListView.as_view(), name="tag-list"),
    path("tag-detail/<int:pk>/", TagDetailView.as_view(), name="tag-detail"),
]


app_name = "tasks"