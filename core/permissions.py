from rest_framework import permissions


class IsAdminOrSelf(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        elif view.action in ['retrieve', 'update', 'partial_update']:
            return obj == request.user
        else:
            return False
