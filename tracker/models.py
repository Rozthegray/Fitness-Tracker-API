from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['email']

class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('weightlifting', 'Weightlifting'),
        ('swimming', 'Swimming'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(choices=ACTIVITY_TYPES, max_length=50)
    duration = models.PositiveIntegerField()
    distance = models.FloatField(blank=True, null=True)
    calories_burned = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.activity_type} by {self.user.username}"
