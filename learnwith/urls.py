"""learnwith URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from web.views import HomeView, ExploreView, DetailSubjectView, ProfileView, ProfileEditView, MySubjectsListView, ConfirmBookingView, LearningPlanView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('',HomeView.as_view(), name='home'),
    path('explore/', ExploreView.as_view(), name='explore'),
    path('detail/<int:pk>', DetailSubjectView.as_view(), name="subject-detail"),
    path('accounts/', include('allauth.urls')),
    path('profile/<int:pk>', ProfileView.as_view(), name="profile"),
    path('profile/edit', ProfileEditView.as_view(), name="profile-edit"),
    path('mysubjects/', MySubjectsListView.as_view(), name='mysubjects'),
    path('confirm/<int:id>', ConfirmBookingView.as_view(), name="confirm-booking"),
    path('learningplan/', LearningPlanView.as_view(), name='learningplan' ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)