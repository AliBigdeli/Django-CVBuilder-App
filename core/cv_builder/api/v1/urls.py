# serializers.py
from django.urls import include, path
from . import views

app_name= "api-v1"

urlpatterns = [
    path('profile/',views.ProfileListCreateView.as_view() ,name="profile-list"),
    path('profile/<int:pk>/',views.ProfileDetailView.as_view() ,name="profile-detail"),
    path('profile/<int:profile_id>/work/',views.WorkListCreateView.as_view() ,name="work-list"),
    path('profile/<int:profile_id>/work/<int:work_id>/',views.WorkDetailView.as_view() ,name="work-detail"),
    path('profile/<int:profile_id>/work/move/',views.WorkMoveView.as_view() ,name="work-move"),
    path('profile/<int:profile_id>/education/',views.EducationListCreateView.as_view() ,name="education-list"),
    path('profile/<int:profile_id>/education/<int:education_id>/',views.EducationDetailView.as_view() ,name="education-detail"),
    path('profile/<int:profile_id>/education/move/',views.EducationMoveView.as_view() ,name="education-move"),
    path('profile/<int:profile_id>/skill/',views.SkillListCreateView.as_view() ,name="skill-list"),
    path('profile/<int:profile_id>/skill/<int:skill_id>/',views.SkillDetailView.as_view() ,name="skill-detail"),
    path('profile/<int:profile_id>/skill/move/',views.SkillMoveView.as_view() ,name="skill-move"),
    path('profile/<int:profile_id>/link/',views.LinkListCreateView.as_view() ,name="link-list"),
    path('profile/<int:profile_id>/link/<int:link_id>/',views.LinkDetailView.as_view() ,name="link-detail"),
    path('profile/<int:profile_id>/link/move/',views.LinkMoveView.as_view() ,name="link-move"),
    path('profile/<int:profile_id>/achievement/',views.AchievementListCreateView.as_view() ,name="achievement-list"),
    path('profile/<int:profile_id>/achievement/<int:achievement_id>/',views.AchievementDetailView.as_view() ,name="achievement-detail"),
    path('profile/<int:profile_id>/achievement/move/',views.AchievementMoveView.as_view() ,name="achievement-move"),
    path('profile/<int:profile_id>/affiliate/',views.AffiliateListCreateView.as_view() ,name="affiliate-list"),
    path('profile/<int:profile_id>/affiliate/<int:affiliate_id>/',views.AffiliateDetailView.as_view() ,name="affiliate-detail"),
    path('profile/<int:profile_id>/affiliate/move/',views.AffiliateMoveView.as_view() ,name="affiliate-move"),
    path('profile/<int:profile_id>/certification/',views.CertificationListCreateView.as_view() ,name="certification-list"),
    path('profile/<int:profile_id>/certification/<int:certification_id>/',views.CertificationDetailView.as_view() ,name="certification-detail"),
    path('profile/<int:profile_id>/certification/move/',views.CertificationMoveView.as_view() ,name="certification-move"),
    path('profile/<int:profile_id>/language/',views.LanguageListCreateView.as_view() ,name="language-list"),
    path('profile/<int:profile_id>/language/<int:language_id>/',views.LanguageDetailView.as_view() ,name="language-detail"),
    path('profile/<int:profile_id>/language/move/',views.LanguageMoveView.as_view() ,name="language-move"),
    # path('profile/<int:profile_id>/additional/',views.AdditionalListCreateView.as_view() ,name="additional-list"),
    # path('profile/<int:profile_id>/additional/<int:additional_id>/',views.AdditionalDetailView.as_view() ,name="additional-detail"),
]
