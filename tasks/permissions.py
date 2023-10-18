from rest_framework import permissions

class IsSuperuserOrReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in ['POST', 'DELETE'] and request.user.is_superuser:
            return True

        if request.method in ['GET', 'PUT', 'PATCH']:
            print("Passed")
            return request.user.is_authenticated

        return False
