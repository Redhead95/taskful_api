import os
import uuid
from django.db import models
from django.utils.deconstruct import deconstructible


@deconstructible
class GenerateHouseImagePath(object):
    def __init__(self):
        pass

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        path = f'houses/{instance.id}/images/'
        name = f'main.{ext}'
        return os.path.join(path, name)


house_image_path = GenerateHouseImagePath()


class House(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    image = models.FileField(upload_to=house_image_path, blank=True, null=True)
    description = models.TextField()
    points = models.IntegerField(default=0)
    completed_tasks_count = models.IntegerField(default=0)
    notcompleted_tasks_count = models.IntegerField(default=0)
    manager = models.OneToOneField('user.profile', on_delete=models.SET_NULL, blank=True, null=True, related_name='managed_house')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} | {self.name}'
