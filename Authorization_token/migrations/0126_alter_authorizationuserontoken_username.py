# Generated by Django 5.1.2 on 2024-12-23 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authorization_token', '0125_alter_authorizationuserontoken_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorizationuserontoken',
            name='username',
            field=models.CharField(blank=True, default='*t7OpQc/+b', max_length=150, unique=True),
        ),
    ]
