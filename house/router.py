from django.db import router
from rest_framework import routers
from .viewsets import HouseViewSet

app_name = 'house'
router = routers.DefaultRouter()
router.register('house', HouseViewSet)
