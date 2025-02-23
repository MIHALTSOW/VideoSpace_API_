from django.urls import re_path

from Comments.consumers import CommentsPhotoConsumer

websocket_urlpatterns = [
    re_path(r"ws/comments-photo/(?P<pk>\d+)/$", CommentsPhotoConsumer.as_asgi()),
]
