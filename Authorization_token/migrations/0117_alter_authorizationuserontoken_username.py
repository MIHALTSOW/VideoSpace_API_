# Generated by Django 5.1.2 on 2024-12-16 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authorization_token', '0116_alter_authorizationuserontoken_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorizationuserontoken',
            name='username',
            field=models.CharField(blank=True, default='G#7(&^S"x8', max_length=150, unique=True),
        ),
    ]
