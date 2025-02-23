import django_filters
from django_filters import FilterSet, CharFilter, DateTimeFilter, NumberFilter

from Authorization_token.models import AuthorizationUserOnToken
from .models import Photo, Video


class PhotoFilter(FilterSet):
    created_after = DateTimeFilter(field_name='created_at', lookup_expr='gte', label='Created after')
    created_before = DateTimeFilter(field_name='created_at', lookup_expr='lte', label='Created before')
    title = CharFilter(field_name='title', lookup_expr='icontains')
    category = CharFilter(field_name='category', lookup_expr='icontains')
    username = CharFilter(field_name='user__username', lookup_expr='icontains')
    user_id = NumberFilter(field_name='user_id', lookup_expr='exact')

    class Meta:
        model = Photo
        fields = ['title', 'category', 'created_after', 'created_before', 'username', 'user_id']




class VideoFilter(django_filters.FilterSet):
    created_after = DateTimeFilter(field_name='created_at', lookup_expr='gte', label='Created after')
    created_before = DateTimeFilter(field_name='created_at', lookup_expr='lte', label='Created before')
    title = CharFilter(field_name='title', lookup_expr='icontains')
    category = CharFilter(field_name='category', lookup_expr='in')

    class Meta:
        model = Video
        fields = ['title', 'category', 'created_after', 'created_before']