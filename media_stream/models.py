from django.db import models
from multiselectfield import MultiSelectField

from .utils import Filters


# Create your models here.
class Video(models.Model):
    """Create fields for video model."""

    title = models.CharField(max_length=150)
    description = models.TextField()
    category = MultiSelectField(choices=Filters.get_filter_types())
    video = models.FileField(upload_to="videos/", max_length=255)
    thumbnail = models.ImageField(upload_to="thumbnails/", blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Photo(models.Model):
    """Create fields for photo model."""

    title = models.CharField(max_length=150)
    description = models.TextField()
    category = MultiSelectField(choices=Filters.get_filter_types())
    photo = models.ImageField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(
        "Authorization_token.AuthorizationUserOnToken", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
