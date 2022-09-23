from django.conf import settings
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import JsonResponse
from django.views.generic import ListView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView

from ads.models import User
from ads.serializers import UserCreateSerializer, UserListSerializer, UserDetailSerializer, UserUpdateSerializer


# class UserListView(ListView):
# model = User
# queryset = User.objects.all()

# def get(self, request, *args, **kwargs):
# super().get(request, *args, **kwargs)
# self.object_list = self.object_list.annotate(total_ads=Count('ad'))

# paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
# page_number = request.GET.get('page')
# page_obj = paginator.get_page(page_number)

# return JsonResponse({
# 'items': [
# {'id': user.id,
# 'first_name': user.first_name,
# 'last_name': user.last_name,
# 'username': user.username,
# 'role': user.role,
# 'age': user.age,
# 'locations': list(map(str, user.locations.all())),
# 'total_ads': user.total_ads} for user in page_obj
# ],
# 'num_pages': page_obj.paginator.num_pages,
# 'total': page_obj.paginator.count
# })

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
