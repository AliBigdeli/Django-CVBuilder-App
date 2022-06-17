from django.shortcuts import render, get_object_or_404
from django.urls import reverse,reverse_lazy
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, UpdateView, TemplateView, CreateView, DeleteView, FormView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from cv_builder.forms import UserProfileForm
from cv_builder.models import *
# Create your views here.


class DashboardIndex(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'


class DashboardProfileListView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/profile_list.html'

class DashboardProfileCreateView(LoginRequiredMixin,CreateView):
    template_name = 'dashboard/profile_create.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('dashboard:profile-list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form) 

class DashboardProfileEditView(LoginRequiredMixin,UpdateView):
    template_name = 'dashboard/profile_edit.html'
    form_class = UserProfileForm
    queryset = UserProfile.objects.all()
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_id"] = self.get_object().id
        return context
    
    def get_success_url(self):
        return reverse('dashboard:profile-edit',kwargs={'pk':self.get_object().id})
         

class DashboardWorkView(LoginRequiredMixin, DetailView):
    template_name = 'dashboard/profile_work_mgmt.html'
    queryset = UserProfile.objects.all()
    
class DashboardEducationView(LoginRequiredMixin, DetailView):
    template_name = 'dashboard/profile_education_mgmt.html'
    queryset = UserProfile.objects.all()

class DashboardSkillView(LoginRequiredMixin, DetailView):
    template_name = 'dashboard/profile_skill_mgmt.html'
    queryset = UserProfile.objects.all()
    

class DashboardLinkView(LoginRequiredMixin, DetailView):
    template_name = 'dashboard/profile_link_mgmt.html'
    queryset = UserProfile.objects.all()
    
class DashboardAchievementView(LoginRequiredMixin, DetailView):
    template_name = 'dashboard/profile_achievement_mgmt.html'
    queryset = UserProfile.objects.all()
    
class DashboardAffiliateView(LoginRequiredMixin, DetailView):
    template_name = 'dashboard/profile_affiliate_mgmt.html'
    queryset = UserProfile.objects.all()

class DashboardCertificationView(LoginRequiredMixin, DetailView):
    template_name = 'dashboard/profile_certification_mgmt.html'
    queryset = UserProfile.objects.all()
    
class DashboardLanguageView(LoginRequiredMixin, DetailView):
    template_name = 'dashboard/profile_language_mgmt.html'
    queryset = UserProfile.objects.all()
    

class DashboardMoreView(LoginRequiredMixin, DetailView):
    template_name = 'dashboard/profile_more_mgmt.html'
    queryset = UserProfile.objects.all()
    

class DashboardFinalizeView(LoginRequiredMixin, DetailView):
    template_name = 'dashboard/profile_finalize_mgmt.html'
    queryset = UserProfile.objects.all()
    
    
class DashboardTemplateShowView(LoginRequiredMixin, DetailView):
    template_name = 'cv_sample/sample_1.html'
    queryset = UserProfile.objects.all()
    
    def get_context_data(self, **kwargs):
        response = super().get_context_data(**kwargs)
        response["skills"] = Skill.objects.filter(profile=self.get_object()).order_by("order")
        response["works"] = WorkExperience.objects.filter(profile=self.get_object()).order_by("order")
        response["educations"] = EducationExperience.objects.filter(profile=self.get_object()).order_by("order")
        response["achievements"] = Achievement.objects.filter(profile=self.get_object()).order_by("order")
        response["affiliates"] = Affiliate.objects.filter(profile=self.get_object()).order_by("order")
        response["links"] = Link.objects.filter(profile=self.get_object()).order_by("order")
        response["certifications"] = Certification.objects.filter(profile=self.get_object()).order_by("order")
        response["languages"] = Language.objects.filter(profile=self.get_object()).order_by("order")
        return response