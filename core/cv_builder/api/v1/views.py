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


class WorkMoveView(generics.GenericAPIView):
    serializer_class = WorkOrderSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_order = serializer.validated_data['order']
        obj = get_object_or_404(WorkExperience,pk=serializer.validated_data['item_id'])
        # Make sure we received an order
        if new_order is None:
            return Response(
                data={'error': 'No order given'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Make sure our new order is not below one
        if int(new_order) < 1:
            return Response(
                data={'error': 'Order cannot be zero or below'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        WorkExperience.objects.move(obj, new_order)

        return Response({'success': True, 'order': new_order})


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



class EducationMoveView(generics.GenericAPIView):
    serializer_class = EducationOrderSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_order = serializer.validated_data['order']
        obj = get_object_or_404(EducationExperience,pk=serializer.validated_data['item_id'])
        # Make sure we received an order
        if new_order is None:
            return Response(
                data={'error': 'No order given'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Make sure our new order is not below one
        if int(new_order) < 1:
            return Response(
                data={'error': 'Order cannot be zero or below'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        EducationExperience.objects.move(obj, new_order)

        return Response({'success': True, 'order': new_order})



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


class SkillMoveView(generics.GenericAPIView):
    serializer_class = SkillOrderSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_order = serializer.validated_data['order']
        obj = get_object_or_404(Skill,pk=serializer.validated_data['item_id'])
        # Make sure we received an order
        if new_order is None:
            return Response(
                data={'error': 'No order given'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Make sure our new order is not below one
        if int(new_order) < 1:
            return Response(
                data={'error': 'Order cannot be zero or below'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        Skill.objects.move(obj, new_order)

        return Response({'success': True, 'order': new_order})

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


class LinkMoveView(generics.GenericAPIView):
    serializer_class = LinkOrderSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_order = serializer.validated_data['order']
        obj = get_object_or_404(Link,pk=serializer.validated_data['item_id'])
        # Make sure we received an order
        if new_order is None:
            return Response(
                data={'error': 'No order given'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Make sure our new order is not below one
        if int(new_order) < 1:
            return Response(
                data={'error': 'Order cannot be zero or below'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        Link.objects.move(obj, new_order)

        return Response({'success': True, 'order': new_order})

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

class AchievementMoveView(generics.GenericAPIView):
    serializer_class = AchievementOrderSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_order = serializer.validated_data['order']
        obj = get_object_or_404(Achievement,pk=serializer.validated_data['item_id'])
        # Make sure we received an order
        if new_order is None:
            return Response(
                data={'error': 'No order given'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Make sure our new order is not below one
        if int(new_order) < 1:
            return Response(
                data={'error': 'Order cannot be zero or below'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        Achievement.objects.move(obj, new_order)

        return Response({'success': True, 'order': new_order})


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

class CertificationMoveView(generics.GenericAPIView):
    serializer_class = CertificationOrderSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_order = serializer.validated_data['order']
        obj = get_object_or_404(Certification,pk=serializer.validated_data['item_id'])
        # Make sure we received an order
        if new_order is None:
            return Response(
                data={'error': 'No order given'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Make sure our new order is not below one
        if int(new_order) < 1:
            return Response(
                data={'error': 'Order cannot be zero or below'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        Certification.objects.move(obj, new_order)

        return Response({'success': True, 'order': new_order})



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

class LanguageMoveView(generics.GenericAPIView):
    serializer_class = LanguageOrderSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_order = serializer.validated_data['order']
        obj = get_object_or_404(Language,pk=serializer.validated_data['item_id'])
        # Make sure we received an order
        if new_order is None:
            return Response(
                data={'error': 'No order given'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Make sure our new order is not below one
        if int(new_order) < 1:
            return Response(
                data={'error': 'Order cannot be zero or below'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        Language.objects.move(obj, new_order)

        return Response({'success': True, 'order': new_order})