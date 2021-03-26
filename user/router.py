from django.db import router
from rest_framework import routers
from .viewsets import UserViewSet, ProfileViewSet

app_name = "user"

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('profile', ProfileViewSet)
