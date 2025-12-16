from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    # Custom permissions which only allow the owners of an object to inherit it.

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed at any request,
        # So we'll always allow GET, HEAD or or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        else :
            return False
        

        