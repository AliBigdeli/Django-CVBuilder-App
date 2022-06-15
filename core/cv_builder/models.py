from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from accounts.models import User
from django.db import models
import os
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError


class UserProfile(models.Model):
    GENDER_CHOICE = (("M", "Male"), ("F", "Female"), ("O", "Other"))
    avatar = models.ImageField(upload_to="images/avatar/", blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    about = models.TextField
    email = models.EmailField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_avatar(self):
        try:
            return self.avatar.url
        except:
            return ""



class WorkExperience(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    employer = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    description = models.TextField()
    start_month = models.CharField(max_length=5)
    start_year = models.CharField(max_length=5)
    still_work = models.BooleanField(default=False)
    end_month = models.CharField(max_length=5)
    end_year = models.CharField(max_length=5)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.profile} - {self.title}"


class EducationExperience(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    university_name = models.CharField(max_length=255)
    university_location = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field = models.CharField(max_length=255)    
    still_educate = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    end_month = models.CharField(max_length=5)
    end_year = models.CharField(max_length=5)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.profile} - {self.title}"

class Skill(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.profile} - {self.name}"



class Links(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    url = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.profile} - {self.url}"


class Achievement(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.profile} - {self.title}"


class Affiliation(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.profile} - {self.title}"
    

class Certification(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.profile} - {self.title}"

class Additional(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.profile}"

class Language(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    LANGUAGE_LEVEL = ((1, "Native"),(2, "Beginner"),(3, "Elementary"), (4, "Intermediate"), (5, "Upper intermediate")
                      (6, "Advanced"), (7, "Proficient"))
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=255, choices=LANGUAGE_LEVEL,default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.profile} - {self.name}"




