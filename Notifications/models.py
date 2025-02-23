from django.db import models


# Create your models here.
class NotificationsOnPhotos(models.Model):
    photo = models.ForeignKey(
        "media_stream.Photo",
        on_delete=models.CASCADE,
        related_name="photo_notifications",
        verbose_name="Фото"
    )
    message = models.ForeignKey(
        "Comments.CommentsPhoto",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Комментарий"
    )
    user = models.ForeignKey(
        "Authorization_token.AuthorizationUserOnToken",
        on_delete=models.CASCADE,
        related_name="notifications",
        verbose_name="Пользователь"
    )
    is_seen = models.BooleanField(default=False, verbose_name="Прочитано?")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return f"Notification for {self.photo} - Seen: {self.is_seen}"

    class Meta:
        verbose_name = "Уведомление для фото"
        verbose_name_plural = "Уведомления для фото"
