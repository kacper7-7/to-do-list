from django.db import models

COMPLETED_CHOICES = [
    ("not done", "NOT DONE"),
    ("done", "DONE")
]

class Tag(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline_datetime = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True, related_name="tasks")

