from rest_framework import serializers

from .models import Video, Photo


class VideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class PhotoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

