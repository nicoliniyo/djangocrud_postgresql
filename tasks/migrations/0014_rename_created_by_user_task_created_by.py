# Generated by Django 5.0.4 on 2024-05-02 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0013_remove_answer_created_by_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='created_by_user',
            new_name='created_by',
        ),
    ]