# Generated by Django 5.0.3 on 2024-03-19 18:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quillpost',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='quillpost',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='quillpost',
            name='title',
            field=models.CharField(default='', max_length=150),
        ),
    ]
