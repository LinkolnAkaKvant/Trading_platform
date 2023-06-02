from rest_framework import permissions


class IsActiveStaffPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff and request.user.is_active
