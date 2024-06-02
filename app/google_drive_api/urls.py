# Django imports
from django.urls import path

# imprort views
from google_drive_api.views import create_google_doc

urlpatterns = [
    path('create_google_doc/', create_google_doc, name="create_google_doc"),
]