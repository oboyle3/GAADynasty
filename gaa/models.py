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
    
class Player(models.Model):

    POSITIONS = [
        ("GK", "Goalkeeper"),
        ("RB", "Right Back"),
        ("FB", "Full Back"),
        ("LB", "Left Back"),
        ("RHB", "Right Half Back"),
        ("CB", "Center Back"),
        ("LHB", "Left Half Back"),
        ("RMF", "Right Midfield"),
        ("LMF", "Left Midfield"),
        ("RHF", "Right Half Forward"),
        ("CHF", "Center Half Forward"),
        ("LHF", "Left Half Forward"),
        ("RCF", "Right Corner Forward"),
        ("CF", "Full Forward"),
        ("LCF", "Left Corner Forward"),
    ]

    name = models.CharField(max_length=100)

    club = models.ForeignKey(
        GAAClub,
        on_delete=models.CASCADE,
        related_name="players"
    )

    position = models.CharField(
        max_length=5,
        choices=POSITIONS
    )

    overall_rating = models.IntegerField()

    speed = models.IntegerField()
    stamina = models.IntegerField()
    skill = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.club.name})"


class Season(models.Model):
    OFFENSIVE_STYLES = [
        ("BAL", "Balanced"),
        ("ATT", "Attacking"),
        ("DEF", "Defensive"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="season"
    )

    coached_club = models.ForeignKey(
        GAAClub,
        on_delete=models.CASCADE
    )

    offensive_style = models.CharField(
        max_length=3,
        choices=OFFENSIVE_STYLES,
        default="BAL"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} coaching {self.coached_club.name}"





class Author(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    # a book has a title
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    # a book has a author
    total_copies = models.IntegerField(default=1)
    #a book has a total amount of total copies

    def __str__(self):
        return self.title