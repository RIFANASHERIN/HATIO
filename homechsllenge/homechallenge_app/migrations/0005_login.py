# Generated by Django 4.0.1 on 2024-05-24 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homechallenge_app', '0004_rename_project_todolist_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]