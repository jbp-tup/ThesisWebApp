from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_initial = models.TextField(max_length=3)

    def __str__(self):
        return f'{self.user.username} Profile'
