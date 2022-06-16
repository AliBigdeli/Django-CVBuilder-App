from rest_framework.fields import ReadOnlyField
from rest_framework import permissions, serializers, status
from django.urls import reverse
from ...models import *
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request', None)
        validated_data['user'] = request.user
        return super().create(validated_data)


class WorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkExperience
        fields = ['id', 'order', 'title', 'employer', 'city', 'country', 'description',
                  'start_month', 'start_year', 'still_work', 'end_month', 'end_year']
        read_only_fields = ['order']

    def validate(self, attrs):
        request = self.context.get('request', None)
        url_parameter = request.parser_context['kwargs'].get("profile_id")
        if url_parameter:
            attrs["profile"] = get_object_or_404(
                UserProfile, pk=url_parameter, user=request.user)
        return super().validate(attrs)


class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = EducationExperience
        fields = ['id', 'order', 'university_name', 'university_location', 'degree', 'field', 'description',
                  'start_month', 'start_year', 'still_educate', "description", 'end_month', 'end_year']
        read_only_fields = ['order']

    def validate(self, attrs):
        request = self.context.get('request', None)
        url_parameter = request.parser_context['kwargs'].get("profile_id")
        if url_parameter:
            attrs["profile"] = get_object_or_404(
                UserProfile, pk=url_parameter, user=request.user)
        return super().validate(attrs)


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ['id', 'order', 'name']
        read_only_fields = ['order']

    def validate(self, attrs):
        request = self.context.get('request', None)
        url_parameter = request.parser_context['kwargs'].get("profile_id")
        if url_parameter:
            attrs["profile"] = get_object_or_404(
                UserProfile, pk=url_parameter, user=request.user)
        return super().validate(attrs)
    
class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = ['id', 'order', 'url']
        read_only_fields = ['order']

    def validate(self, attrs):
        request = self.context.get('request', None)
        url_parameter = request.parser_context['kwargs'].get("profile_id")
        if url_parameter:
            attrs["profile"] = get_object_or_404(
                UserProfile, pk=url_parameter, user=request.user)
        return super().validate(attrs)
    

class AchievementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achievement
        fields = ['id', 'order', 'title','description']
        read_only_fields = ['order']

    def validate(self, attrs):
        request = self.context.get('request', None)
        url_parameter = request.parser_context['kwargs'].get("profile_id")
        if url_parameter:
            attrs["profile"] = get_object_or_404(
                UserProfile, pk=url_parameter, user=request.user)
        return super().validate(attrs)
    

class AffiliateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Affiliate
        fields = ['id', 'order', 'title','description']
        read_only_fields = ['order']

    def validate(self, attrs):
        request = self.context.get('request', None)
        url_parameter = request.parser_context['kwargs'].get("profile_id")
        if url_parameter:
            attrs["profile"] = get_object_or_404(
                UserProfile, pk=url_parameter, user=request.user)
        return super().validate(attrs)
    
    
class CertificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certification
        fields = ['id', 'order', 'title','description']
        read_only_fields = ['order']

    def validate(self, attrs):
        request = self.context.get('request', None)
        url_parameter = request.parser_context['kwargs'].get("profile_id")
        if url_parameter:
            attrs["profile"] = get_object_or_404(
                UserProfile, pk=url_parameter, user=request.user)
        return super().validate(attrs)
    

class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ['id', 'order', 'name','level']
        read_only_fields = ['order']

    def validate(self, attrs):
        request = self.context.get('request', None)
        url_parameter = request.parser_context['kwargs'].get("profile_id")
        if url_parameter:
            attrs["profile"] = get_object_or_404(
                UserProfile, pk=url_parameter, user=request.user)
        return super().validate(attrs)




class WorkOrderSerializer(serializers.Serializer):
    order = serializers.IntegerField(required=True)
    item_id = serializers.IntegerField(required=True)
    def validate(self, attrs):
        if attrs.get('order') is None:
            raise serializers.ValidationError({'details':'please provide an ordering'})
        return super().validate(attrs)