# Generated by Django 4.0 on 2022-05-16 14:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='nick_name',
            field=models.CharField(default='unknown', max_length=10, unique=True),
        ),
        migrations.CreateModel(
            name='NickName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(max_length=10)),
                ('in_use', models.BooleanField(default='false')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.baseuser')),
            ],
            options={
                'db_table': 'nick_name',
            },
        ),
    ]
