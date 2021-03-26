import os
import uuid
from django.db import models
from django.utils.deconstruct import deconstructible

NOT_COMPLETE = 'NC'
COMPLETE = 'C'
TASK_STATUS_CHOICES = [
    (NOT_COMPLETE, 'Not Complete'),
    (COMPLETE, 'Complete'),
]


@deconstructible
class GenerateAttachmentFilePath(object):
    def __init__(self):
        pass

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        path = f'task/{instance.task.id}/attachments/'
        name = f'{instance.id}.{ext}'
        return os.path.join(path, name)


attachment_file_path = GenerateAttachmentFilePath()


class TaskList(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=2, choices=TASK_STATUS_CHOICES, default=NOT_COMPLETE)
    house = models.ForeignKey('house.House', on_delete=models.CASCADE, related_name='lists')
    created_by = models.ForeignKey('user.Profile', blank=True, null=True, on_delete=models.SET_NULL, related_name='lists')
    completed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} | {self.name}'


class Task(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=2, choices=TASK_STATUS_CHOICES, default=NOT_COMPLETE)
    task_list = models.ForeignKey('task.TaskList', default=1, on_delete=models.CASCADE, related_name='tasks')
    created_by = models.ForeignKey('user.Profile', blank=True, null=True, on_delete=models.SET_NULL, related_name='created_tasks')
    completed_by = models.ForeignKey('user.Profile', blank=True, null=True, on_delete=models.SET_NULL, related_name='completed_tasks')
    completed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} | {self.name}'


class Attachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task = models.ForeignKey('task.Task', on_delete=models.CASCADE, related_name='attachments')
    file_path = models.FileField(upload_to=attachment_file_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} | {self.task}'
