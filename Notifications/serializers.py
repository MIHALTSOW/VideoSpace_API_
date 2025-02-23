from rest_framework import serializers

from .models import NotificationsOnPhotos



class PhotoNotificationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = NotificationsOnPhotos
        fields = ['id', 'photo', 'user', 'message', 'is_seen', 'date']
