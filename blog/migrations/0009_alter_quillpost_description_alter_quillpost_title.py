# Generated by Django 5.0.3 on 2024-03-19 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_quillpost_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quillpost',
            name='description',
            field=models.TextField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='quillpost',
            name='title',
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
    ]
