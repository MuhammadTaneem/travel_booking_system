from rest_framework import permissions


class IsManagerOrCounterUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user has 'manager' or 'counter' user_type
        return request.user.user_type in ['manager', 'counter']
