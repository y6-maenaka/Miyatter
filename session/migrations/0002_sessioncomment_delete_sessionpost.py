# Generated by Django 4.0 on 2022-05-11 16:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('session', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionComment',
            fields=[
                ('comment_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('comment_content', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.baseuser')),
            ],
            options={
                'db_table': 'session_comment',
            },
        ),
        migrations.DeleteModel(
            name='SessionPost',
        ),
    ]
