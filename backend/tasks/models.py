from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=255)  # Task title
    description = models.TextField(blank=True, null=True)  # Optional description
    completed = models.BooleanField(default=False)  # Task status
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when updated

    def __str__(self):
        return self.title  # Show title in admin panel
