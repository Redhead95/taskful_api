from rest_framework import serializers
from .models import TaskList, Task, Attachment
from house.models import House


class TaskListSerializer(serializers.ModelSerializer):

    house = serializers.HyperlinkedRelatedField(queryset=House.objects.all(), many=False, view_name='house-detail')
    created_by = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name='profile-detail')
    tasks = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='task-detail')

    class Meta:
        model = TaskList
        fields = (
            'url',
            'id',
            'name',
            'description',
            'status',
            'house',
            'tasks',
            'created_by',
            'completed_at',
            'created_at',
            'updated_at',
        )
        read_only_fields = [
            'status',
            'completed_at',
            'created_by',
            'created_at',
            'updated_at',
        ]


class TaskSerializer(serializers.ModelSerializer):

    created_by = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name='profile-detail')
    completed_by = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name='profile-detail')
    task_list = serializers.HyperlinkedRelatedField(queryset=TaskList.objects.all(), many=False, view_name='tasklist-detail')
    attachments = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='attachment-detail')

    def validate_task_list(self, value):
        user_profile = self.context['request'].user.profile
        if value not in user_profile.house.lists.all():
            raise serializers.ValidationError('Tasklist provided does not belong to house for which user is member.')
        return value

    def create(self, validated_data):
        user_profile = self.context['request'].user.profile
        task = Task.objects.create(**validated_data)
        task.created_by = user_profile
        task.save()
        return task

    class Meta:
        model = Task
        fields = (
            'url',
            'id',
            'name',
            'description',
            'status',
            'task_list',
            'attachments',
            'created_by',
            'completed_by',
            'completed_at',
            'created_at',
            'updated_at',
        )
        read_only_fields = [
            'status',
            'created_by',
            'completed_by',
            'completed_at',
            'created_at',
            'updated_at',
        ]


class AttachmentSerializer(serializers.ModelSerializer):

    task = serializers.HyperlinkedRelatedField(queryset=Task.objects.all(), many=False, view_name='task-detail')

    def validate_task_list(self, attrs):
        user_profile = self.context['request'].user.profile
        task = attrs.get('task')
        task_list = TaskList.objects.get(tasks__id__exact=task.id)
        if task_list not in user_profile.house.lists.all():
            raise serializers.ValidationError({'task': 'Task provided does not belong to house for which user is member.'})
        return attrs

    class Meta:
        model = Attachment
        fields = (
            'url',
            'id',
            'task',
            'file_path',
            'created_at',
            'updated_at',
        )
        read_only_fields = [
            'created_at',
            'updated_at',
        ]
