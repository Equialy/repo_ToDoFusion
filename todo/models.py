from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_done = models.DateTimeField(null=True, blank=True)
    time_update = models.DateTimeField(auto_now=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self ):
        return self.title

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]