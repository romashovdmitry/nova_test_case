# Python imports
import os

# Django imports
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

application = get_asgi_application()
