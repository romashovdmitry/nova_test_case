# Django imports
from django.urls import path

# imprort views
from main.views import create_google_doc

urlpatterns = [
    path('api/v1/google_drive/create_google_doc/', create_google_doc, name="create_google_doc"),
]