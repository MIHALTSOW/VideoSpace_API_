# Generated by Django 5.1.2 on 2025-01-02 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authorization_token', '0143_alter_authorizationuserontoken_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorizationuserontoken',
            name='username',
            field=models.CharField(blank=True, default='0>gG.WbZsS', max_length=150, unique=True),
        ),
    ]
