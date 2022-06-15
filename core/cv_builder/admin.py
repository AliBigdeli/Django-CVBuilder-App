from django.contrib import admin

# Register your models here.
from .models import *

class ResumeAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('profile','title','created_date')
    list_filter = ('profile','created_date')
    search_fields = ['profile']

class ResumeFileAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('profile','file','created_date')
    list_filter = ('created_date',)

class VideoIntroFileAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('profile','file','created_date')
    list_filter = ('created_date',)

class EducationExperienceAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('resume','grade','field','still_educate','created_date')
    list_filter = ('created_date','resume','grade','still_educate')

class WorkExperienceAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('resume','title','company','still_work','created_date')
    list_filter = ('created_date','still_work')

class AchievementAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('resume','title','created_date')
    list_filter = ('created_date','resume')

class SocialAccountAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('resume','type','created_date')
    list_filter = ('created_date','resume')

class LanguageAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('resume','name','grade','created_date')
    list_filter = ('created_date','resume')

class SkillAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('resume','name','level','created_date')
    list_filter = ('created_date','resume')

admin.site.register(Resume,ResumeAdmin)
admin.site.register(EducationExperience,EducationExperienceAdmin)
admin.site.register(WorkExperience,WorkExperienceAdmin)
admin.site.register(Achievement,AchievementAdmin)
admin.site.register(ResumeFile,ResumeFileAdmin)
admin.site.register(VideoIntroFile,VideoIntroFileAdmin)
admin.site.register(ResumeSkill)
admin.site.register(ResumeLocation)
admin.site.register(SocialAccount,SocialAccountAdmin)
admin.site.register(Language,LanguageAdmin)
admin.site.register(Skill,SkillAdmin)