# Generated by Django 3.2.4 on 2021-06-18 15:44

import accounts_app.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customusermodel',
            managers=[
                ('objects', accounts_app.models.CustomUserManager()),
            ],
        ),
    ]