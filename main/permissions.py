from rest_framework.permissions import BasePermission


class OnlyStaffCanDeletedObjectPermission(BasePermission):
    message = "Only the administrator can delete."

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method != "DELETE":
            return True

        return bool(request.user and request.user.is_staff)
