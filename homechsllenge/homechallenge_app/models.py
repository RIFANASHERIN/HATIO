from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Project(models.Model):
    title=models.CharField(max_length=100)
    todos=models.IntegerField()
    created_date=models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)



class Todolist(models.Model):
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    description=models.CharField(max_length=500)
    status=models.BooleanField(default=False)
    updated_date=models.DateField()

