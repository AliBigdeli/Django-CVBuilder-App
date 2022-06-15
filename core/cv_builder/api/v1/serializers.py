from rest_framework.fields import ReadOnlyField
from rest_framework import permissions, serializers,status
from django.urls import reverse
from ...models import *
from django.contrib.auth import get_user_model

class ResumeLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeLocation
        fields = ["id","name"]
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        # rep['location'] = ResumeLocationSerializer(instance.location).data
        return rep
        


def get_resume_object(self):
    user = self.context['request'].user
    profile = EmployeeProfile.objects.get(user = user)
    try:
        return Resume.objects.get(profile=profile)
    except (Resume.DoesNotExist, AssertionError):
            raise serializers.ValidationError(detail={"detail":"There is no resume assigned to this user"},code=status.HTTP_404_NOT_FOUND)

class SocialAccountSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = SocialAccount
        fields = ['id', 'type', 'url']

    def create(self, validated_data):
        validated_data.update({"resume": get_resume_object(self)})
        return super().create(validated_data)
        


class WorkExperienceSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = WorkExperience
        fields = ['id','title', 'company', 'still_work',
                  'description', 'start_date', 'end_date']

    def create(self, validated_data):        
        validated_data.update({"resume": get_resume_object(self)})
        return super().create(validated_data)


class EducationExperienceSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = EducationExperience
        fields = ['id', 'grade', 'field',
                  'score', 'university', 'still_educate', 'description', 'start_date', 'end_date']

    def create(self, validated_data):        
        validated_data.update({"resume": get_resume_object(self)})
        return super().create(validated_data)


class AchievementSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Achievement
        fields = ['id','title', 'description',
                  'image', 'url']

    def create(self, validated_data):        
        validated_data.update({"resume": get_resume_object(self)})
        return super().create(validated_data)

class LanguageSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Language
        fields = ['id','name', 'grade']

    def create(self, validated_data):        
        validated_data.update({"resume": get_resume_object(self)})
        return super().create(validated_data)

class SkillSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Skill
        fields = ['id','name', 'level']

    def create(self, validated_data):        
        validated_data.update({"resume": get_resume_object(self)})
        return super().create(validated_data)


class ResumeFileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= ResumeFile
        fields = ["id","file"]
        read_only_fields = ["id"]

class VideoIntroFileSerializer(serializers.ModelSerializer):
    class Meta:
        model= VideoIntroFile
        fields = ["id","file","status"]
        read_only_fields = ["id","status"]
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["status"] = {
            "id": instance.status,
            "name": instance.get_status_display()
        }
        return rep
    def update(self, instance, validated_data):
        instance.status = 2
        instance.save()
        return super().update(instance, validated_data)

class ResumeSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeSkill
        fields = ["id","name"]



class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['id','title',"about", 'married','skill','location']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["skill"] = ResumeSkillSerializer(instance.skill,many=True, context={'request': self.context.get('request', None)}).data
        rep["location"] = ResumeLocationSerializer(instance.location, context={'request': self.context.get('request', None)}).data
        return rep


