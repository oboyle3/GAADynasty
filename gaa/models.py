from django.db import models
from django.contrib.auth.models import User #what does this do?

class GAAClub(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
# 

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_club = models.ForeignKey(
        GAAClub,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    def __str__(self):
        return self.user.username