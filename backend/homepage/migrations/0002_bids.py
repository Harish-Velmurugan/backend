# Generated by Django 3.0.6 on 2020-05-10 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('sid', models.IntegerField()),
                ('uid', models.IntegerField()),
                ('bids', models.IntegerField()),
            ],
        ),
    ]
