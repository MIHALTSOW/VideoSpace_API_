# Generated by Django 5.1.2 on 2024-11-19 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authorization_token', '0011_alter_authorizationuserontoken_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorizationuserontoken',
            name='username',
            field=models.CharField(blank=True, default='HTF#7ATYz\\', max_length=150, unique=True),
        ),
    ]
