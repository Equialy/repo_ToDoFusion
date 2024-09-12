from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse





class Todo(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название заметки')
    content = models.TextField(blank=True, verbose_name='Содержание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_done = models.DateTimeField(null=True, blank=True, verbose_name='Время завершения')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    important = models.BooleanField(default=False, verbose_name='Важно')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Categories', on_delete=models.PROTECT,null=True, blank=True, verbose_name='Категория')


    def __str__(self ):
        return self.title

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

class Categories(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Наименование категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_name', kwargs={'category_slug': self.slug})