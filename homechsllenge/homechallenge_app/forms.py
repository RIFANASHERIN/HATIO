from django import forms
from .models import Project, Todolist

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'todos']

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ['description']
