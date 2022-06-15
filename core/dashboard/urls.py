from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "dashboard"

urlpatterns = [
    path("",views.DashboardIndex.as_view(),name="index"),
    path("profile/list/",views.DashboardProfileListView.as_view(),name="profile-list"),
    # path("profile/create/",views.DashboardProfileCreateView.as_view(),name="profile-create"),
    # path("profile/<int:pk>/edit/",views.DashboardProfileEditView.as_view(),name="profile-edit"),
    # path("profile/<int:pk>/work/",views.DashboardWorkView.as_view(),name="work-mgmt"),
    # path("profile/<int:pk>/education/",views.DashboardEducationView.as_view(),name="education-mgmt"),
    # path("profile/<int:pk>/skill/",views.DashboardSkillView.as_view(),name="skill-mgmt"),
    # path("profile/<int:pk>/link/",views.DashboardLinkView.as_view(),name="link-mgmt"),
    # path("profile/<int:pk>/achievement/",views.DashboardAchievementView.as_view(),name="achievement-mgmt"),
    # path("profile/<int:pk>/affiliate/",views.DashboardAffiliateView.as_view(),name="affiliate-mgmt"),
    # path("profile/<int:pk>/certification/",views.DashboardCertificationView.as_view(),name="certification-mgmt"),
    # path("profile/<int:pk>/language/",views.DashboardLanguageView.as_view(),name="language-mgmt"),
    # path("profile/<int:pk>/additional/",views.DashboardAdditionalView.as_view(),name="additional-mgmt"),
]

