from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from Comments.models import CommentsPhoto


class FilterCommentPhotoListSerializer(serializers.ListSerializer):
    """ Фильтр комментариев только parents """

    def to_representation(self, data):
        """ Фильтр комментариев только parents """
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """ Вывод рекурсивно children """

    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


class CommentPhotoSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    text = serializers.CharField(required=True)
    children = RecursiveSerializer(many=True, required=False)
    deleted = serializers.BooleanField(read_only=True, default=False)

    class Meta:
        # list_serializer_class = FilterCommentPhotoListSerializer
        model = CommentsPhoto
        fields = ['id', 'parent', 'photo', 'user', 'text', 'created_at',
                  'updated_at', 'deleted', 'children']
