from django.urls import path

from .views import CommentsPhotoView, CreateCommentView

urlpatterns = [
    path('comments-photo', CreateCommentView.as_view(), name='comments-photo'),
    path('comments-photo/<int:pk>/', CommentsPhotoView.as_view(), name='comments-photo-detail'),
]
