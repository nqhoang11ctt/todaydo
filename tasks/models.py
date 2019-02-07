from django.db import models
from django.utils import timezone


# Create your models here.
class TaskQuerySet(models.query.QuerySet):
    pass

class TaskManager(models.Manager):
    pass

class Task(models.Model):
    PRIORITY_CHOICES = (
        ('high', 'High'),
        ('low', 'Low'),
        )

    title   =   models.TextField(max_length=200)
    done    =   models.BooleanField(default=False)
    priority=   models.CharField(choices=PRIORITY_CHOICES, default='low', max_length=5)
    time    =   models.TimeField(default=timezone.now)