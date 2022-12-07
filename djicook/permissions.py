from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    message = "You are not Authorize to Access"
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.user == request.user