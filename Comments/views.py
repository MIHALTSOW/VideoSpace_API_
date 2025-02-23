from rest_framework import generics

from Notifications.models import NotificationsOnPhotos
from .models import CommentsPhoto
from .permissions import IsAuthorComment
from .serializers import CommentPhotoSerializer


# Create your views here.
class CommentsPhotoView(generics.UpdateAPIView,
                        generics.DestroyAPIView,
                        generics.ListAPIView):
    """ CRUD for comments """
    permission_classes = [IsAuthorComment]
    queryset = CommentsPhoto.objects.filter(deleted=False)
    serializer_class = CommentPhotoSerializer


    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()


class CreateCommentView(generics.CreateAPIView):
    permission_classes = [IsAuthorComment]
    queryset = CommentsPhoto.objects.filter(deleted=False)
    serializer_class = CommentPhotoSerializer


    def perform_create(self, serializer):
        parent_id = self.request.data.get('parent', None)
        parent_comment = None
        if parent_id:
            parent_comment = CommentsPhoto.objects.get(id=parent_id)

        comment = serializer.save(user=self.request.user, parent=parent_comment)
        photo_owner = comment.photo.user

        NotificationsOnPhotos.objects.create(
            photo=comment.photo,
            message=comment,
            user=photo_owner,
            is_seen=False
        )
