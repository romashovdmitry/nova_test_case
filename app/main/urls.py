# Django imports
from django.urls import path, include

urlpatterns = [
    path("api/v1/google_drive_api/", include("google_drive_api.urls"))
]