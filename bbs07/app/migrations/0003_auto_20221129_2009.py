# Generated by Django 3.2 on 2022-11-29 20:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_comment_content_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='content_time',
        ),
        migrations.AddField(
            model_name='comment',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
