# Generated by Django 4.0.1 on 2024-05-23 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homechallenge_app', '0002_todolist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='todos',
            field=models.IntegerField(),
        ),
    ]
