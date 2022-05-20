# Generated by Django 4.0 on 2022-05-19 13:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_in_use_nickname_is_using_nickname_updated_at'),
        ('session', '0013_session_session_department_session_session_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationSessionoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('session_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='session.session')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.baseuser')),
            ],
            options={
                'db_table': 'registration_session',
            },
        ),
    ]
