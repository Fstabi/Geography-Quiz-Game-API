from rest_framework.permissions import BasePermission


class IsAdminUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Allow any user to list challenges (GET request)
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Restrict access to admin users for all
        # other methods (POST, PUT, PATCH, DELETE)
        return request.user and request.user.is_staff
