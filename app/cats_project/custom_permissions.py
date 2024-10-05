from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.db.models import Model


def IsOwnerOrReadOnly(path_to_owners: list[str]):
    """
    Permission class for checking if the object's owner is the same as the user
    or if the request method is a safe method.

    Args:
        path_to_owners (list): A list of fields to traverse to find the owner
        of the object.
    """
    class WrapperContent(BasePermission):
        def has_permission(self, request, view):
            # if method not GET then it 100% POST then just check auth
            return (request.method in SAFE_METHODS or
                    request.user.is_authenticated)

        def has_object_permission(self, request, view, obj: Model) -> bool:
            if request.method in SAFE_METHODS:
                return True
            owner: Model = obj
            for field in path_to_owners:
                owner = getattr(owner, field)
            return request.user == owner

    return WrapperContent