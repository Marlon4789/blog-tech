# Generated by Django 5.0.3 on 2024-03-21 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_quillpost_description_alter_quillpost_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quillpost',
            name='content',
            field=models.TextField(),
        ),
    ]
