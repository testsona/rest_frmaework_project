from django.db import models

# Create your models here.

class Reminder(models.Model):
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    reminder_type = models.CharField(max_length=10, choices=[('SMS', 'SMS'), ('Email', 'Email')])
    

    def __str__(self):
        return self.message