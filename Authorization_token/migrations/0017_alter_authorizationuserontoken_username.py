# Generated by Django 5.1.2 on 2024-11-22 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authorization_token', '0016_alter_authorizationuserontoken_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorizationuserontoken',
            name='username',
            field=models.CharField(blank=True, default='tM+bo~@veV', max_length=150, unique=True),
        ),
    ]
