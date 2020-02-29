from rest_framework import status, generics, mixins, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ConsultantComment, SoldTimeSlotRate
from .serializers import CommentSerializer, SoldTimeSlotRateSerializer
from .permissions import CommentOwnerPermission, SoldTimeSlotRateOwnerPermission
from .filtersets import CommentFilterSet


class CommentListView(generics.ListCreateAPIView):
    queryset = ConsultantComment.objects.all().order_by('-created')
    serializer_class = CommentSerializer
    permission_classes = [CommentOwnerPermission, permissions.IsAuthenticatedOrReadOnly]
    filterset_class = CommentFilterSet


class CommentDetailView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = ConsultantComment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SoldTimeSlotRateListView(generics.ListCreateAPIView):
    queryset = SoldTimeSlotRate.objects.all()
    serializer_class = SoldTimeSlotRateSerializer
    permission_classes = [SoldTimeSlotRateOwnerPermission, permissions.IsAuthenticatedOrReadOnly]
