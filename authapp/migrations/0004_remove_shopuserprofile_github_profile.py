# Generated by Django 3.2 on 2022-01-08 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_shopuserprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopuserprofile',
            name='github_profile',
        ),
    ]