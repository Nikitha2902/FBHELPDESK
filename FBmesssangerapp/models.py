from django.db import models

# Create your models here.
    
class UserProfile(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    full_name = models.CharField(max_length=255)
    # You can add more fields like date of birth, address, etc.

    def __str__(self):
        return self.email