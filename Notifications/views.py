from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import NotificationsOnPhotos
from .serializers import PhotoNotificationSerializer


class PhotoNotificationView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PhotoNotificationSerializer

    def get_queryset(self):
        return NotificationsOnPhotos.objects.filter(user=self.request.user)
