from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):

    GENDERS = (
        ('m', 'Male'),
        ('f', 'Female'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='profiles/')
    gender = models.CharField(max_length=5, choices = GENDERS)

class Topic(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class Subject(models.Model):
    name = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, related_name='subjects', on_delete=models.CASCADE)
    description = models.TextField()
    user = models.ForeignKey(User, related_name='subjects', on_delete=models.CASCADE)

    def __str__(self):
        return self.name