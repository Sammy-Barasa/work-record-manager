from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.

class Team(models.Model):
    owned_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='team_owner')
    team_name = models.CharField(unique=True,max_length=200)
    logo = models.ImageField(blank=True,null=True)
    members = models.ManyToManyField(
        User, through='TeamMembership',
        related_name='member_of_team',
        through_fields=('team', 'writer')
        )

    def __str__(self):
        return f"{self.team_name} owned by,{self.owned_by}"

class TeamMembership(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='team_owner')
    writer = models.ForeignKey(
        User, on_delete=models.CASCADE,related_name='team_writer')
    date_invited = models.DateTimeField(auto_now=True)
    is_request_accepted = models.BooleanField(default=False)
    date_joined = models.DateTimeField()

    def __str__(self):
        return f"{self.writer_name} member of {self.team_name} joined in {self.date_joined}"
