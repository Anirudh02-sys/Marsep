from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    contact_number=models.BigIntegerField()
    typeofusr = models.CharField(max_length=20)

    def _str_(self):
        return f"{self.username}"