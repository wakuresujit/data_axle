from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hire_date = models.DateField()

class EventType(models.Model):
    name = models.CharField(max_length=100)
    template = models.TextField()

class Event(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    event_date = models.DateField()
    sent_status = models.BooleanField(default=False)
    error_message = models.TextField(blank=True, null=True)


class BirthdayEventType(EventType):
    pass
