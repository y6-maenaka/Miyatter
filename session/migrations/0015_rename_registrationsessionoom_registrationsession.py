# Generated by Django 4.0 on 2022-05-19 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_in_use_nickname_is_using_nickname_updated_at'),
        ('session', '0014_registrationsessionoom'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RegistrationSessionoom',
            new_name='RegistrationSession',
        ),
    ]
