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
from .paginations import *


User = get_user_model()


class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {}
    search_fields = ['first_name', 'last_name',
                     'about', 'email', 'phone_number']
    ordering_fields = []
    pagination_class = DefaultPagination


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]


class WorkListCreateView(generics.ListCreateAPIView):
    serializer_class = WorkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return WorkExperience.objects.filter(profile__id=self.kwargs.get('profile_id')).order_by("order")


class WorkDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(WorkExperience, pk=self.kwargs.get('work_id'), profile__id=self.kwargs.get('profile_id'))


class EducationListCreateView(generics.ListCreateAPIView):
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return EducationExperience.objects.filter(profile__id=self.kwargs.get('profile_id')).order_by("order")


class EducationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(EducationExperience, pk=self.kwargs.get('education_id'), profile__id=self.kwargs.get('profile_id'))


class SkillListCreateView(generics.ListCreateAPIView):
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Skill.objects.filter(profile__id=self.kwargs.get('profile_id')).order_by("order")


class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Skill, pk=self.kwargs.get('skill_id'), profile__id=self.kwargs.get('profile_id'))


class LinkListCreateView(generics.ListCreateAPIView):
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Link.objects.filter(profile__id=self.kwargs.get('profile_id')).order_by("order")


class LinkDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Link, pk=self.kwargs.get('link_id'), profile__id=self.kwargs.get('profile_id'))


class AchievementListCreateView(generics.ListCreateAPIView):
    serializer_class = AchievementSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Achievement.objects.filter(profile__id=self.kwargs.get('profile_id')).order_by("order")


class AchievementDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AchievementSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Achievement, pk=self.kwargs.get('achievement_id'), profile__id=self.kwargs.get('profile_id'))


class CertificationListCreateView(generics.ListCreateAPIView):
    serializer_class = CertificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Certification.objects.filter(profile__id=self.kwargs.get('profile_id')).order_by("order")


class CertificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CertificationSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Certification, pk=self.kwargs.get('certification_id'), profile__id=self.kwargs.get('profile_id'))


class LanguageListCreateView(generics.ListCreateAPIView):
    serializer_class = LanguageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Language.objects.filter(profile__id=self.kwargs.get('profile_id')).order_by("order")


class LanguageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LanguageSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Language, pk=self.kwargs.get('language_id'), profile__id=self.kwargs.get('profile_id'))
