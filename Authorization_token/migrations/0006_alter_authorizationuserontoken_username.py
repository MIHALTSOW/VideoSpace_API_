# Generated by Django 5.1.2 on 2024-11-15 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authorization_token', '0005_alter_authorizationuserontoken_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorizationuserontoken',
            name='username',
            field=models.CharField(blank=True, default='vy0!>!YajP', max_length=150, unique=True),
        ),
    ]
