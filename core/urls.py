from django.urls import path
from .views import TaskListView, TaskDetailView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task-detail/<int:pk>/", TaskDetailView.as_view(), name="task-detail")
]


app_name = "tasks"