from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Profile, Topic, Subject, LearningDate, SubjectSubscription
# Register your models here.

class SubjectAdmin(SummernoteModelAdmin):
    summernote_fields = ('additional_information')

admin.site.register(Profile)
admin.site.register(Topic)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(LearningDate)
admin.site.register(SubjectSubscription)