# Generated by Django 4.2.1 on 2024-09-12 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_categories_todo_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='todo.categories'),
        ),
    ]