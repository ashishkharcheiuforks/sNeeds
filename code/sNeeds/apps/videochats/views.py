from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import JsonResponse
from django.utils import timezone
from django.utils.timezone import now
from django.conf import settings

from rest_framework import status, generics, mixins, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from sNeeds.utils import skyroom
from ..consultants.models import ConsultantProfile

from .models import Room
from .serializers import RoomSerializer
from .permissions import RoomOwnerPermission


class RoomListView(generics.ListAPIView):
    serializer_class = RoomSerializer
    filterset_fields = ('sold_time_slot',)
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if ConsultantProfile.objects.filter(user=user).exists():
            # TODO: Order by start_time
            qs = Room.objects.filter(sold_time_slot__consultant__user=user).order_by("-created")
        else:
            qs = Room.objects.filter(sold_time_slot__sold_to=user).order_by("-created")
        return qs


class RoomDetailAPIView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated, RoomOwnerPermission]
