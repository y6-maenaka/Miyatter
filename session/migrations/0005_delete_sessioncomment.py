# Generated by Django 4.0 on 2022-05-13 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0004_sessionhistory_sessioncomment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SessionComment',
        ),
    ]
