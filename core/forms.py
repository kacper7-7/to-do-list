from django import forms
from .models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'deadline_datetime', 'tags', 'is_completed']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
