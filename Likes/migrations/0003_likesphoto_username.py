# Generated by Django 5.1.2 on 2024-11-17 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Likes', '0002_alter_likesphoto_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='likesphoto',
            name='username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
