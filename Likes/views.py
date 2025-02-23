from django.db.models import F
from drf_spectacular.utils import extend_schema
from rest_framework import status, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from media_stream.models import Photo
from .models import LikesPhoto
from .serializers import PhotoLikeSerializer


class CreateLikeView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=['likes'],
        request=PhotoLikeSerializer,
        responses={
            200: PhotoLikeSerializer
        })
    def post(self, request):
        photo_id = request.data.get('photo', None)

        if not photo_id:
            return Response({'error': 'Photo ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = request.user
        photo = get_object_or_404(Photo, id=photo_id)

        like_instance, created = LikesPhoto.objects.get_or_create(user=user, photo=photo)

        if created:
            like_instance.username = user.username
            like_instance.save()
            photo.likes = F('likes') + 1
        else:
            like_instance.delete()
            photo.likes = F('likes') - 1

        photo.save(update_fields=['likes'])
        photo.refresh_from_db(fields=['likes'])

        serializer = PhotoLikeSerializer(like_instance)

        return Response({
            "user_id": serializer.data['user_id'],
            "user": serializer.data['user'],
            "photo_id": serializer.data['photo'],
            "likes": photo.likes,

        }, status=status.HTTP_200_OK)


class GetUserLikes(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PhotoLikeSerializer

    def get_queryset(self):
        user = self.request.user
        return LikesPhoto.objects.filter(user=user)
