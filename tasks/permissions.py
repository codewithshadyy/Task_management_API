
from rest_framework import permissions

class ISAuthorOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user