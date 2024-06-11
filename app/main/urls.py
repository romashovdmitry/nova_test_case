# Django imports
from django.urls import path, include

# Swagger imports
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("api/v1/google_drive_api/", include("google_drive_api.urls")),
    # Swagger urls
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]

# https://docs.djangoproject.com/en/5.0/howto/static-files/#serving-static-files-during-development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)