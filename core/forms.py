from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'deadline_datetime', 'tags', 'is_completed']