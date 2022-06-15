from rest_framework import viewsets, generics, mixins, views
from rest_framework import pagination, status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from ...models import *
from .serializers import *
from django.contrib.auth import get_user_model




class ResumeApiView(generics.RetrieveUpdateAPIView):
    """
    A simple Generic view to retrive and update resume
    """
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            # queryset just for schema generation metadata
            return Resume.objects.none()
        return super().get_queryset()
    
    def get_object(self):
        # queryset = self.get_queryset()
        # profile = EmployeeProfile.objects.get(user=self.request.user)
        # return get_object_or_404(queryset, profile=profile)
        return get_object_or_404(Resume, profile__user__id=self.request.user.id)


class SocialAccountApiViewSet(viewsets.ModelViewSet):
    """
    A simple viewset to retrive and update and remove social accounts
    """
    serializer_class = SocialAccountSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            # queryset just for schema generation metadata
            return SocialAccount.objects.none()
        return SocialAccount.objects.filter(resume__profile__user=self.request.user)


class WorkExperienceApiViewSet(viewsets.ModelViewSet):
    """
    A simple viewset to retrive and update and remove Work experience
    """
    serializer_class = WorkExperienceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            # queryset just for schema generation metadata
            return WorkExperience.objects.none()
        return WorkExperience.objects.filter(resume__profile__user=self.request.user)


class EducationExperienceApiViewSet(viewsets.ModelViewSet):
    """
    A simple viewset to retrive and update and remove education experiences
    """
    serializer_class = EducationExperienceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            # queryset just for schema generation metadata
            return EducationExperience.objects.none()
        return EducationExperience.objects.filter(resume__profile__user=self.request.user)


class AchievementApiViewSet(viewsets.ModelViewSet):
    """
    A simple viewset to retrive and update and remove achievements
    """

    serializer_class = AchievementSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            # queryset just for schema generation metadata
            return Achievement.objects.none()
        return Achievement.objects.filter(resume__profile__user=self.request.user)


class LanguageApiViewSet(viewsets.ModelViewSet):
    """
    A simple viewset to retrive and update and remove language
    """

    serializer_class = LanguageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            # queryset just for schema generation metadata
            return Language.objects.none()
        return Language.objects.filter(resume__profile__user=self.request.user)


class SkillApiViewSet(viewsets.ModelViewSet):
    """
    A simple viewset to retrive and update and remove language
    """

    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            # queryset just for schema generation metadata
            return Skill.objects.none()
        return Skill.objects.filter(resume__profile__user=self.request.user)

class FullResumeApiView(views.APIView):
    """

    """
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(EmployeeProfile, user=self.request.user.id)
     

    def get(self, request, *args, **kwargs):
        profile = self.get_object()
        resume = Resume.objects.get(profile=profile)
        socials = SocialAccount.objects.filter(resume=resume)
        educations = EducationExperience.objects.filter(resume=resume)
        experiences = WorkExperience.objects.filter(resume=resume)
        achievements = Achievement.objects.filter(resume=resume)
        languages = Language.objects.filter(resume=resume)
        data = {"profile": UserProfile(profile, many=False).data,
                "resume": ResumeSerializer(resume).data,
                "socials": SocialAccountSerializer(socials, many=True).data,
                "educations": EducationExperienceSerializer(educations, many=True).data,
                "experiences": WorkExperienceSerializer(experiences, many=True).data,
                "achievements": AchievementSerializer(achievements, many=True).data,
                "languages": LanguageSerializer(languages, many=True).data
                }
        return Response(data)


class PreviewFullResumeApiView(views.APIView):

    permission_classes = [IsAuthenticated]
    lookup_field = "pk"

    def get_object(self):
        return get_object_or_404(EmployeeProfile, user__pk=self.kwargs['pk'])


    def get(self, request, *args, **kwargs):
        profile = self.get_object()
        resume = Resume.objects.get(profile=profile)
        socials = SocialAccount.objects.filter(resume=resume)
        educations = EducationExperience.objects.filter(resume=resume)
        experiences = WorkExperience.objects.filter(resume=resume)
        achievements = Achievement.objects.filter(resume=resume)
        languages = Language.objects.filter(resume=resume)
        data = {"profile": UserProfile(profile, many=False).data,
                "resume": ResumeSerializer(resume).data,
                "socials": SocialAccountSerializer(socials, many=True).data,
                "educations": EducationExperienceSerializer(educations, many=True).data,
                "experiences": WorkExperienceSerializer(experiences, many=True).data,
                "achievements": AchievementSerializer(achievements, many=True).data,
                "languages": LanguageSerializer(languages, many=True).data,
                }
        return Response(data)


class ResumeFileApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ResumeFileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            # queryset just for schema generation metadata
            return ResumeFile.objects.none()
        return super().get_queryset()
    
    def get_object(self):
        return ResumeFile.objects.get(profile__user=self.request.user)

    def delete(self, request, *args, **kwargs):
        resume_instance = self.get_object()
        resume_instance.file.delete()
        resume_instance.save()
        return Response({"detail":["resume file deleted successfully"]},status=status.HTTP_200_OK)
    

class VideoIntroFileApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VideoIntroFileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            # queryset just for schema generation metadata
            return VideoIntroFile.objects.none()
        return super().get_queryset()
    
    def get_object(self):
        return VideoIntroFile.objects.get(profile__user=self.request.user.id)

    def delete(self, request, *args, **kwargs):
        resume_instance = self.get_object()
        resume_instance.file.delete()
        resume_instance.status=1
        resume_instance.save()
        return Response({"detail":["video file deleted successfully"]},status=status.HTTP_200_OK)

class ResumeLocationApiView(generics.ListAPIView):
    queryset = ResumeLocation.objects.all()
    serializer_class = ResumeLocationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ResumeSkillApiView(generics.ListAPIView):
    queryset = ResumeSkill.objects.all()
    serializer_class = ResumeSkillSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]