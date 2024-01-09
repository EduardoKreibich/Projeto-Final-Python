from rest_framework import permissions
from rest_framework.views import View
from .models import Content


class IsAccountAdminOrStudent(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Content) -> bool:
        print(obj)
        return (
            request.user.is_superuser
            or request.user in obj.course.students.all()
            and request.method in permissions.SAFE_METHODS
        )
