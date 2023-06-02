from rest_framework import permissions


class IsActiveStaffPermission(permissions.BasePermission):
    """
    Пермишн, разрешающий пользоваться API только активным пользователям и staff персоналу.
    """
    def has_permission(self, request, view):
        return request.user and (request.user.is_staff or request.user.is_active)
