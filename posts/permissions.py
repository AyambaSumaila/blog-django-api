from rest_framework import permissions  # type: ignore

class BasePermissions(object):
    
    def has_permission(self, request, view):
        return True
    

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permissions(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True