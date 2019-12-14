from django.db import models
from django.contrib.auth.models import User

class AppUser(User):
    is_admin = models.CharField(max_length=100)
    
