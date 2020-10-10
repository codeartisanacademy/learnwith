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

    def __str__(self):
        return self.user.first_name
    
    @property
    def full_name(self):
        return '{0} {1}'.format(self.user.first_name, self.user.last_name)

    @property
    def full_name_with_greeting(self):
        full_name_with_greeting = ''
        if self.gender == 'm':
            full_name_with_greeting = '{0}. {1} {2}'.format("Mr", self.user.first_name, self.user.last_name)
        else:
            full_name_with_greeting = '{0}. {1} {2}'.format("Mrs.", self.user.first_name, self.user.last_name)

        return full_name_with_greeting


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
    picture = models.ImageField(null=True, blank=True, upload_to="subjects/")
    additional_information = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name