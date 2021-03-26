from django.db import router
from rest_framework import routers
from .viewsets import TaskListViewSet, TaskViewSet, AttachmentViewSet

app_name = 'task'

router = routers.DefaultRouter()
router.register('task_list', TaskListViewSet)
router.register('task', TaskViewSet)
router.register('attachment', AttachmentViewSet)
