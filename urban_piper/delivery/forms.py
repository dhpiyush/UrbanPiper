from django import forms
from django.forms import (
    DateField,
    EmailInput,
    PasswordInput,
    Select,
    TextInput,
    BooleanField,
)
from delivery.models import Tasks
from delivery.widgets import CustomDateInput


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        exclude = ["created_by", "accepted_by", "completed_on", "created_on"]

        labels = {
            "title": "Task name",
            "created_on": "Task Created On",
            "completed_on": "Task Completed On",
            "status": "Task Status",
            "priority": "Priority",
            "accepted_by": "Accepted By",
        }
