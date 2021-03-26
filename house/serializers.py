from rest_framework import serializers
from .models import House


class HouseSerializer(serializers.ModelSerializer):
    members = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='profile-detail')
    members_count = serializers.IntegerField(read_only=True)
    manager = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name='profile-detail')
    lists = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='tasklist-detail')

    class Meta:
        model = House
        fields = [
            'url',
            'id',
            'image',
            'name',
            'manager',
            'description',
            'members',
            'members_count',
            'points',
            'completed_tasks_count',
            'notcompleted_tasks_count',
            'lists',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'members_count',
            'points',
            'completed_tasks_count',
            'notcompleted_tasks_count',
            'created_at',
            'updated_at',
        ]
