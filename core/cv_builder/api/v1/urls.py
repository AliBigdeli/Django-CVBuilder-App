# serializers.py
from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('social-account', SocialAccountApiViewSet, basename='social-account')
router.register('work-experience', WorkExperienceApiViewSet, basename='work-experience')
router.register('education-experience', EducationExperienceApiViewSet, basename='education-experience')
router.register('achievement', AchievementApiViewSet, basename='achievement')
router.register('language', LanguageApiViewSet, basename='language')
router.register('skill', SkillApiViewSet, basename='skill')

urlpatterns = [
    path("resume/",ResumeApiView.as_view(),name="resume"),
    path("resume/review/",FullResumeApiView.as_view(),name="full-resume"),
    # path("resume/<int:pk>/review/",PreviewFullResumeApiView.as_view(),name="full-resume-preview"),
    path("resume/file/",ResumeFileApiView.as_view(),name="resume-file"),
    path("resume/video/",VideoIntroFileApiView.as_view(),name="resume-video"),
    path("resume/location/list/",ResumeLocationApiView.as_view(),name="resume-location-list"),
    path("resume/skill/list/",ResumeSkillApiView.as_view(),name="resume-skill-list"),
    path('', include(router.urls)),
]
