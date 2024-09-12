from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название заметки')
    content = models.TextField(blank=True, verbose_name='Содержание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_done = models.DateTimeField(null=True, blank=True, verbose_name='Время завершения')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    important = models.BooleanField(default=False, verbose_name='Важно')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self ):
        return self.title

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]