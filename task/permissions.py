from rest_framework import permissions


class IsAllowedToEditTaskListElseNone(permissions.BasePermission):
    """Only allow the creator editing permission"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        return request.user.profile == obj.created_by


class IsAllowedToEditTaskElseNone(permissions.BasePermission):
    """Only allow the creator editing permission"""

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.profile.house != None

        return False

    def has_object_permission(self, request, view, obj):
        return request.user.profile.house == obj.task_list.house


class IsAllowedToEditAttachmentElseNone(permissions.BasePermission):
    """Only allow the creator editing permission"""

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.profile.house != None

        return False

    def has_object_permission(self, request, view, obj):
        return request.user.profile.house == obj.task.task_list.house
