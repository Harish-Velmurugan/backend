# Generated by Django 3.0.6 on 2020-05-10 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20200510_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_personal',
            name='dob',
        ),
    ]
