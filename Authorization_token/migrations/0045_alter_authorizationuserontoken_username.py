# Generated by Django 5.1.2 on 2024-12-16 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authorization_token', '0044_alter_authorizationuserontoken_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorizationuserontoken',
            name='username',
            field=models.CharField(blank=True, default=")Y'<,h'>wK", max_length=150, unique=True),
        ),
    ]
