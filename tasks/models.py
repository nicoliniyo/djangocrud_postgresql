from django.db import models
from django.utils import timezone
from .constants import default_user
from .constants import default_engine

# Create your models here.
class Task(models.Model):
    input_value = models.CharField(max_length=100)

    # Timestamp field with default value of current time
    created_at = models.DateTimeField(default=timezone.now)
    created_by_user = models.CharField(default=default_user)
    # String field for engine
    engine = models.CharField(max_length=50, default=default_engine)  # Adjust max_length as needed

class Answer(models.Model):
    answer_value = models.TextField(blank=False)

    # Timestamp field with default value of current time
    created_at = models.DateTimeField(default=timezone.now)
    created_by_user = models.CharField(default=default_user)
    # String field for engine
    engine = models.CharField(max_length=50, default=default_engine)  # Adjust max_length as needed
    # Foreign key to Task model
    task = models.ForeignKey(Task, on_delete=models.CASCADE)