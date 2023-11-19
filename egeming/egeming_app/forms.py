from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['subject_type', 'task_number', 'title', 'task_condition', 'points']
