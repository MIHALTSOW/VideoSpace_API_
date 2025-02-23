from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .filters import PhotoFilter, VideoFilter
from .models import Video, Photo
from .serializers import VideoListSerializer, PhotoListSerializer
from .swagger_params import video_photo_search_params


class VideoAndPhotoPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 6


class VideoList(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('?')
    serializer_class = VideoListSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = VideoAndPhotoPagination
    search_fields = ['title', 'description', 'category']
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = VideoFilter

    @extend_schema(
        tags=['videos'],
        parameters=video_photo_search_params,
        responses={200: VideoListSerializer}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PhotoList(viewsets.ModelViewSet):
    queryset = Photo.objects.all().order_by('?')
    serializer_class = PhotoListSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = VideoAndPhotoPagination
    search_fields = ['title', 'description', 'category']
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = PhotoFilter

    @extend_schema(
        tags=['photos'],
        parameters=video_photo_search_params,
        responses={200: PhotoListSerializer}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)



