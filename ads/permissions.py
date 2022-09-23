from rest_framework import permissions

from ads.models import Selection, User, Ad


class SelectionUpdatePermission(permissions.BasePermission):
    message = 'You can not touch this selection'

    def has_permission(self, request, view):
        try:
            selection = Selection.objects.get(pk=view.kwargs['pk'])
        except Selection.DoesNotExist:
            return False

        if selection.owner.id == request.juser.id:
            return True
        elif request.user.role != User.Role.MEMBER:
            return True
        else:
            return False

class AdUpdateDeletePermission(permissions.BasePermission):
    message = 'You can not touch this selection'

    def has_permission(self, request, view):
        try:
            selection = Ad.objects.get(pk=view.kwargs['pk'])
        except Selection.DoesNotExist:
            return False

        if selection.author.id == request.juser.id:
            return True
        elif request.user.role != User.Role.MEMBER:
            return True
        else:
            return False


