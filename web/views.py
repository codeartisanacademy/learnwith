from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from web.models import Subject, Profile
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect, reverse

from .forms import ProfileForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'public/home.html'

    def get(self, request):
        subjects = Subject.objects.all().order_by('id')
        return render(request, self.template_name, {'subjects':subjects})

class DetailSubjectView(DetailView):
    model = Subject
    template_name = 'subjects/detail.html'
    context_object_name = 'subject'
    
class ExploreView(TemplateView):
    template_name = 'public/explore.html'

    def get(self, request):
        return render(request, self.template_name)

class ProfileView(DetailView):
    model = Profile
    template_name = 'account/profile.html'
    context_object_name = 'profile'

class ProfileEditView(TemplateView):
    template_name = 'account/edit_profile.html'

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        form = ProfileForm(instance=profile)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        profile = Profile.objects.get(user=request.user)
        form = ProfileForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('profile'))
        else: 
            return render(request, self.template_name, {'form':form})
