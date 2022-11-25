from django.db import models


class Task(models.Model):
    """Model definition for Task."""

    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expired_at = models.DateTimeField()
    author_id = models.IntegerField()
    assignee_id = models.IntegerField()
    state = 
    priority = 

    class Meta:
        """Meta definition for Task."""

        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        """Unicode representation of Task."""
        pass

CharField, TextField, IntegerField, DateTimeField


:date