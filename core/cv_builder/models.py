from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from accounts.models import User
from django.db import models
import os
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.db import models,transaction
from django.db.models import F, Max


class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    EXPERIENCE_LEVEL = ((1, "0-3 Years"), (2, "3-5 Years"), (3, "5-10 Years"),(4, "10+ Years"))
    avatar = models.ImageField(
        upload_to="images/avatar/", blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255,blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=255)
    country = models.CharField(max_length=255)
    years_level = models.IntegerField(choices=EXPERIENCE_LEVEL,default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_avatar(self):
        try:
            return self.avatar.url
        except:
            return ""
    class Meta:
        ordering = ('-created_date',)

class OrderManager(models.Manager):
    """ Manager to encapsulate bits of business logic """
    def move(self, obj, new_order):
        """ Move an object to a new order position """

        object_query = self.get_queryset()

        with transaction.atomic():
            if obj.order > int(new_order):
                object_query.filter(
                    profile=obj.profile,
                    order__lt=obj.order,
                    order__gte=new_order,
                ).exclude(
                    pk=obj.pk
                ).update(
                    order=F('order') + 1,
                )
            else:
                object_query.filter(
                    profile=obj.profile,
                    order__lte=new_order,
                    order__gt=obj.order,
                ).exclude(
                    pk=obj.pk,
                ).update(
                    order=F('order') - 1,
                )

            obj.order = new_order
            obj.save()
    
    def create(self, **kwargs):
        instance = self.model(**kwargs)

        with transaction.atomic():
            # Get our current max order number
            results = self.filter(
                profile=instance.profile
            ).aggregate(
                Max('order')
            )

            # Increment and use it for our new object
            current_order = results['order__max']
            if current_order is None:
                current_order = 0
            value = current_order + 1
            instance.order = value
            instance.save()
            return instance

class WorkExperience(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=1,null=True,blank=True)
    title = models.CharField(max_length=255)
    employer = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    description = models.TextField()
    start_month = models.CharField(max_length=5)
    start_year = models.CharField(max_length=5)
    still_work = models.BooleanField(default=False)
    end_month = models.CharField(max_length=5,null=True,blank=True)
    end_year = models.CharField(max_length=5,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = OrderManager()
    
    def __str__(self):
        return f"{self.profile} - {self.title}"


class EducationExperience(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=1,null=True,blank=True)
    university_name = models.CharField(max_length=255)
    university_location = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    start_month = models.CharField(max_length=5,null=True)
    start_year = models.CharField(max_length=5,null=True)
    still_educate = models.BooleanField(default=False)
    end_month = models.CharField(max_length=5,null=True,blank=True)
    end_year = models.CharField(max_length=5,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = OrderManager()
    
    def __str__(self):
        return f"{self.profile} - {self.university_name}"


class Skill(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=1,null=True,blank=True)
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = OrderManager()
    
    def __str__(self):
        return f"{self.profile} - {self.name}"


class Link(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=1,null=True,blank=True)
    url = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = OrderManager()
    
    def __str__(self):
        return f"{self.profile} - {self.url}"


class Achievement(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=1,null=True,blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    objects = OrderManager()
    
    def __str__(self):
        return f"{self.profile} - {self.title}"


class Affiliate(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=1,null=True,blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = OrderManager()
    
    def __str__(self):
        return f"{self.profile} - {self.title}"


class Certification(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=1,null=True,blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = OrderManager()
    
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
    order = models.PositiveIntegerField(default=1,null=True,blank=True)
    LANGUAGE_LEVEL = ((1, "Native"), (2, "Beginner"), (3, "Elementary"),
                      (4, "Intermediate"), (5, "Upper intermediate"),
                      (6, "Advanced"), (7, "Proficient"))
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=255, choices=LANGUAGE_LEVEL, default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = OrderManager()
    
    def __str__(self):
        return f"{self.profile} - {self.name}"
