# Generated by Django 5.1.2 on 2024-12-16 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authorization_token', '0075_alter_authorizationuserontoken_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorizationuserontoken',
            name='username',
            field=models.CharField(blank=True, default='sT[[mUo5\\;', max_length=150, unique=True),
        ),
    ]
