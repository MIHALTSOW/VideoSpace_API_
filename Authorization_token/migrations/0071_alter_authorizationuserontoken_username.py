# Generated by Django 5.1.2 on 2024-12-16 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authorization_token', '0070_alter_authorizationuserontoken_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorizationuserontoken',
            name='username',
            field=models.CharField(blank=True, default='*8;:\\~n8_s', max_length=150, unique=True),
        ),
    ]
