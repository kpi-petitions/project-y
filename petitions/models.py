from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS_CHOICES = (
    ('V', 'Voting'),
    ('A', 'Accepted'),
    ('D', 'Declined'),
)

class Petition(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(User, related_name='petitions')
    deadline = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='V')
    responsible = models.CharField(max_length=50, blank=True, null=True)
    # TODO: mediacontent: photos and video
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)


class PetitionSign(models.Model):
    class Meta:
        unique_together=('author', 'petition')
    author = models.ForeignKey(User, related_name='signed')
    petition = models.ForeignKey(Petition, related_name='signs')
    comment = models.TextField(max_length=200, null=True, blank=True)
    anonymous = models.BooleanField(default=False)