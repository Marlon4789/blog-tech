# Generated by Django 5.0.3 on 2024-03-19 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_quillpost_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quillpost',
            name='image_url',
            field=models.URLField(null=True),
        ),
    ]
