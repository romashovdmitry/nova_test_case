# Django imports
from django.urls import path, include

# Swagger imports
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)

urlpatterns = [
    path("api/v1/google_drive_api/", include("google_drive_api.urls")),
    # Swagger urls
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]