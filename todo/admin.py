from django.contrib import admin
from .models import Todo

class ToDoAdmin(admin.ModelAdmin):
    readonly_fields = ('time_create',)




admin.site.register(Todo, ToDoAdmin)