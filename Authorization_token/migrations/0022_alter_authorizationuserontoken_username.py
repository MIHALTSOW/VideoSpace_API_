# Generated by Django 5.1.2 on 2024-11-25 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authorization_token', '0021_alter_authorizationuserontoken_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorizationuserontoken',
            name='username',
            field=models.CharField(blank=True, default='4&j%sp9(Wx', max_length=150, unique=True),
        ),
    ]
