# Generated by Django 5.1.2 on 2024-11-16 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authorization_token', '0007_alter_authorizationuserontoken_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorizationuserontoken',
            name='username',
            field=models.CharField(blank=True, default='+-xXkW,+{J', max_length=150, unique=True),
        ),
    ]
