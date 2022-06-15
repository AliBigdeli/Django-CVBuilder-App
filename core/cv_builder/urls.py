from django.urls import path, include

app_name = "cv_builder"

urlpatterns = [
    path("api/v1/", include("cv_builder.api.v1.urls")),
]
