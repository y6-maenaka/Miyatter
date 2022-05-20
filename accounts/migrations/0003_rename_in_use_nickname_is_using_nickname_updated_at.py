# Generated by Django 4.0 on 2022-05-19 13:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_baseuser_nick_name_nickname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nickname',
            old_name='in_use',
            new_name='is_using',
        ),
        migrations.AddField(
            model_name='nickname',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]