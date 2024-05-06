# Generated by Django 5.0.4 on 2024-05-06 14:58

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('tasks', '0001_initial'), ('tasks', '0002_task_description_alter_task_title'), ('tasks', '0003_remove_task_description'), ('tasks', '0004_task_description'), ('tasks', '0005_remove_task_description'), ('tasks', '0006_task_description'), ('tasks', '0007_task_created_at_task_engine'), ('tasks', '0008_remove_task_description_task_created_user_and_more'), ('tasks', '0009_rename_created_user_task_created_by_user'), ('tasks', '0010_rename_title_task_input_value'), ('tasks', '0011_answer'), ('tasks', '0012_alter_answer_created_by_user_and_more'), ('tasks', '0013_remove_answer_created_by_user'), ('tasks', '0014_rename_created_by_user_task_created_by')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_value', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('engine', models.CharField(default='AWANLLM', max_length=50)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_value', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('engine', models.CharField(default='AWANLLM', max_length=50)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
    ]