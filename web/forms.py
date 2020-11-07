from django.forms import ModelForm
from django import forms

from .models import Profile, SubjectSubscription

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'gender']

class SubjectSubscriptionForm(ModelForm):
    class Meta:
        model = SubjectSubscription
        fields = '__all__'
        widgets = {'user':forms.HiddenInput(), 'subject':forms.HiddenInput(), 'subscription_date':forms.HiddenInput()}