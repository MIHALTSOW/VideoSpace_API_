# Generated by Django 5.1.2 on 2025-01-05 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authorization_token', '0182_alter_authorizationuserontoken_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorizationuserontoken',
            name='username',
            field=models.CharField(blank=True, default='f0I$iBXdkO', max_length=150, unique=True),
        ),
    ]
