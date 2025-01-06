from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Organiser(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='organiser_profile'  # Unique reverse relation name
    )
    full_name = models.CharField(max_length=200)
    organization_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()  # Removed unique=True
    created_at = models.DateTimeField(default=datetime.today)

    def __str__(self):
        return self.full_name


class Attendee(models.Model):
    HONORIFIC_CHOICES = [
        ('Mr', 'Mr.'),
        ('Mrs', 'Mrs.'),
        ('Ms', 'Ms.'),
        ('Dr', 'Dr.'),
        ('Prof', 'Prof.'),
        ('Other', 'Other')
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='attendee_profile'  # Unique reverse relation name
    )
    organizer = models.ForeignKey(
        Organiser,
        on_delete=models.CASCADE,
        related_name='attendee_list',
          default="Individual"  # Avoids conflict with reverse query name
    )
    honorific = models.CharField(
        max_length=10,
        choices=HONORIFIC_CHOICES,
        default='Mr'
    )
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()  # Removed unique=True
    created_at = models.DateTimeField(default=datetime.today)
    def __str__(self):

        return f"{self.honorific} {self.full_name}"
    

    class Event(models.Model):
     name = models.CharField(max_length=255)  # Event name with max length of 255 characters
    date = models.DateTimeField(default=datetime.today)  # Event date and time
    location = models.CharField(max_length=255,default="")  # Event location
    description = models.TextField(default="")  # Detailed description of the event
    max_participants = models.IntegerField(null=True, blank=True)  # Optional field for max participants
    organizer = models.ForeignKey(User, on_delete=models.CASCADE,null=True)  # Reference to the User model (organizer)

    def __str__(self):
        return self.name  # Returns the name of the event as its string representation