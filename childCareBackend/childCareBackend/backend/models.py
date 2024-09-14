from django.db import models

# Create your models here.
# models.py
from django.db import models

class Registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    parent_email = models.EmailField()
    mobile_number = models.CharField(max_length=15)  # Assuming 15 characters for mobile number
    password = models.CharField(max_length=100)  # Adjust max_length as needed
    confirm_password = models.CharField(max_length=100)  # Adjust max_length as needed

    ROLE_CHOICES = [
        ('Guardian', 'Guardian'),
        ('Employee', 'Employee'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.parent_email})"
