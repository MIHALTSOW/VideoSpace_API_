# Generated by Django 5.1.2 on 2025-01-04 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authorization_token', '0171_alter_authorizationuserontoken_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorizationuserontoken',
            name='username',
            field=models.CharField(blank=True, default='/vYVZ@-5l"', max_length=150, unique=True),
        ),
    ]
