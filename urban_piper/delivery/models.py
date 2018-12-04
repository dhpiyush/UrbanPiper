from django.db import models
from django.contrib.auth.models import User


class Tasks(models.Model):
    STATUS = (
        ("new", "New"),
        ("accepted", "Accepted"),
        ("completed", "Completed"),
        ("declined", "Declined"),
        ("cancelled", "Cancelled"),
    )
    PRIORITY = (("high", "High"), ("medium", "Medium"), ("low", "Low"))

    created_by = models.ForeignKey(User, related_name="creator")
    title = models.CharField(max_length=50)
    priority = models.CharField(max_length=7, choices=PRIORITY)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=12, choices=STATUS)
    accepted_by = models.ForeignKey(
        User, related_name="assignee", blank=True, null=True
    )
    cancelled_by = models.ForeignKey(
        User, related_name="assignee_cancelled", blank=True, null=True
    )
    declined_by = models.ForeignKey(
        User, related_name="assignee_declined", blank=True, null=True
    )
    completed_on = models.DateField(blank=True, null=True)
    accepted_on = models.DateTimeField(blank=True, null=True)
    declined_on = models.DateTimeField(blank=True, null=True)
    cancelled_on = models.DateTimeField(blank=True, null=True)

    def _str_(self):
        return self.title

    def get_completed_on(self):
        return self.completed_on
