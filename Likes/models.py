from django.db import models


# Create your models here.
class LikesPhoto(models.Model):
    user = models.ForeignKey('Authorization_token.AuthorizationUserOnToken', on_delete=models.CASCADE)
    username = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ForeignKey('media_stream.Photo', on_delete=models.CASCADE)

    # # гарантируем уникальность этих полей в таблице
    class Meta:
        unique_together = ('user', 'photo')

    def __str__(self):
        return f'{self.user} лайкнул фото {self.photo}'


class LikesVideo(models.Model):
    user = models.ForeignKey('Authorization_token.AuthorizationUserOnToken', on_delete=models.CASCADE)
    video = models.ForeignKey('media_stream.Video', on_delete=models.CASCADE)

    # гарантируем уникальность этих полей в таблице
    class Meta:
        unique_together = ('user', 'video')

    def __str__(self):
        return f'{self.user} лайкнул видео {self.video}'
