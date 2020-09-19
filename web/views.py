from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from web.models import Subject

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