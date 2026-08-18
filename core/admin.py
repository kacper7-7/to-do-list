from django.contrib import admin

from core.models import Tag, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
