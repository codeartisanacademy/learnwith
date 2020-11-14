from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from web.models import Subject, Profile, LearningDate, SubjectSubscription

from .forms import ProfileForm, SubjectSubscriptionForm

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
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('profile', kwargs={'pk':request.user.id}))
        else: 
            return render(request, self.template_name, {'form':form})

class MySubjectsListView(ListView):
    model = Subject
    
    def get_queryset(self):
        queryset = super(MySubjectsListView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

class ConfirmBookingView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login'
    template_name = 'subjects/confirm.html'
    id = None

    def get(self, request, id):
        learning_date = LearningDate.objects.get(id=id)
        form = SubjectSubscriptionForm(initial={'subject':learning_date.subject, 'user':request.user, 'subscription_date':learning_date.learning_date})
        return render(request, self.template_name, {'learning_date':learning_date, 'form':form })

    def post(self, request, id):
        learning_date = LearningDate.objects.get(id=id)
        form = SubjectSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('subject-detail', kwargs={'pk': learning_date.subject.id }))
        
        else:
            return render(request, self.template_name, {'learning_date':learning_date, 'form':form })


class LearningPlanView(ListView):
    model = SubjectSubscription