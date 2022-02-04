from rest_framework import permissions


class IsAuthorOrReadOnlyPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if (request.method in permissions.SAFE_METHODS
                and request.user.is_authenticated):
            return True
        return obj.author == request.user
