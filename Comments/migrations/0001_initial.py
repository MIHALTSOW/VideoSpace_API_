# Generated by Django 5.1.2 on 2024-11-15 14:13

import django.db.models.deletion
import mptt.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('media_stream', '0003_remove_photo_resized_photo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentsPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('publisher', models.BooleanField(default=True, verbose_name='Опубликовать?')),
                ('deleted', models.BooleanField(default=False, verbose_name='Удалено?')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='Comments.commentsphoto', verbose_name='Дочерний комментарий')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_comments', to='media_stream.photo', verbose_name='Фото')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_photo_comments', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommentsVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('publisher', models.BooleanField(default=True, verbose_name='Опубликовать?')),
                ('deleted', models.BooleanField(default=False, verbose_name='Удалено?')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='Comments.commentsvideo', verbose_name='Дочерний комментарий')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_video_comments', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_comments', to='media_stream.video', verbose_name='Видео')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'abstract': False,
            },
        ),
    ]
