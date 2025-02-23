from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class AbstractComments(models.Model):
    text = models.TextField("Сообщение", max_length=2000)
    created_at = models.DateTimeField("Время создания", auto_now_add=True)
    updated_at = models.DateTimeField("Время обновления", auto_now=True)
    publisher = models.BooleanField("Опубликовать?", default=True)
    deleted = models.BooleanField("Удалено?", default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        abstract = True


class CommentsPhoto(AbstractComments, MPTTModel):
    photo = models.ForeignKey(
        'media_stream.Photo',
        on_delete=models.CASCADE,
        related_name='photo_comments',
        verbose_name='Фото'
    )
    user = models.ForeignKey(
        'Authorization_token.AuthorizationUserOnToken',
        on_delete=models.CASCADE,
        related_name='user_photo_comments',
        verbose_name='Пользователь'
    )
    parent = TreeForeignKey(
        'self',
        verbose_name='Дочерний комментарий',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='children'
    )

    def __str__(self):
        return "{} - {}".format(self.user, self.photo)


class CommentsVideo(AbstractComments, MPTTModel):
    video = models.ForeignKey(
        'media_stream.Video',
        on_delete=models.CASCADE,
        related_name='video_comments',
        verbose_name='Видео'
    )
    user = models.ForeignKey(
        'Authorization_token.AuthorizationUserOnToken',
        on_delete=models.CASCADE,
        related_name='user_video_comments',
        verbose_name='Пользователь'
    )
    parent = TreeForeignKey(
        'self',
        verbose_name='Дочерний комментарий',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='children'
    )

    def __str__(self):
        return "{} - {}".format(self.user, self.video)
