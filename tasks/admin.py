from django.contrib import admin
from .models import Task
from .models import Answer

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
# Register your models here.
admin.site.register(Task, TaskAdmin)
admin.site.register(Answer, TaskAdmin)