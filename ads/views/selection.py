from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Selection
from ads.permissions import SelectionUpdatePermission
from ads.serializers import SelectionListSerializer, SelectionDetailSerializer, SelectionSerializer


class SelectionListView(ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionListSerializer


class SelectionDetailView(RetrieveAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionDetailSerializer


class SelectionUpdateView(UpdateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated, SelectionUpdatePermission]


class SelectionCreateView(CreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated]
