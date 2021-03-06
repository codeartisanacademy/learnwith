from django.db import models
from django.contrib.auth.models import User
import datetime
import pytz

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


class SubjectSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subject_subscriptions')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subcriptions')
    subscription_date = models.DateTimeField()

    def __str__(self):
        return "{0} - {1} at {2}".format(self.user, self.subject, self.subscription_date)


class LearningDate(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='dates')
    learning_date = models.DateTimeField()
    

    def __str__(self):
        return "{0} - {1}".format(self.subject.name, self.learning_date)
    
    @property
    def future_date(self):
        utc = pytz.UTC
        # compare the date with the date of today
        date_1 = utc.localize(self.learning_date)
        date_2 = utc.localize(datetime.datetime.today())
        return  self.learning_date > date_2