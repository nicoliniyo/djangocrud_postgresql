# Generated by Django 5.0.4 on 2024-04-24 20:33

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_rename_title_task_input_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_value', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by_user', models.CharField(default='DEFAULT_USER')),
                ('engine', models.CharField(default='AWANLLM', max_length=50)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
    ]
