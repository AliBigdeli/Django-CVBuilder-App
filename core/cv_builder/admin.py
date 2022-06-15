from django.contrib import admin

# Register your models here.
from .models import *

class UserProfileAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('id','first_name','last_name','email','phone_number','created_date')
    list_filter = ('created_date',)
    search_fields = ['first_name','last_name','email','phone_number','about']

class WorkExperienceAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('id','profile','title','employer','still_work','created_date')
    list_filter = ('created_date','still_work')

class EducationExperienceAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('id','profile','degree','field','still_educate','created_date')
    list_filter = ('created_date','still_educate')

class SkillAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('id','profile','name','created_date')
    list_filter = ('created_date',)


class LinkAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('id','profile','url','created_date')
    list_filter = ('created_date',)


class AchievementAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('id','profile','title','created_date')
    list_filter = ('created_date',)
    
class AffiliateAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('id','profile','title','created_date')
    list_filter = ('created_date',)

class CertificationAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('id','profile','title','created_date')
    list_filter = ('created_date',)

class AdditionalAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('id','profile','created_date')
    list_filter = ('created_date',)

class LanguageAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('id','profile','name','level','created_date')
    list_filter = ('created_date',)



admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(EducationExperience,EducationExperienceAdmin)
admin.site.register(WorkExperience,WorkExperienceAdmin)
admin.site.register(Achievement,AchievementAdmin)
admin.site.register(Link,LinkAdmin)
admin.site.register(Affiliate,AffiliateAdmin)
admin.site.register(Certification,CertificationAdmin)
admin.site.register(Additional,AdditionalAdmin)
admin.site.register(Language,LanguageAdmin)
admin.site.register(Skill,SkillAdmin)