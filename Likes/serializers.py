from rest_framework import serializers

from media_stream.models import Photo
from .models import LikesPhoto


class PhotoLikeSerializer(serializers.ModelSerializer):
    likes = serializers.ReadOnlyField(source='photo.likes')
    user = serializers.CharField(read_only=True)
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = LikesPhoto
        fields = ['user_id', 'user', 'photo', 'likes']
