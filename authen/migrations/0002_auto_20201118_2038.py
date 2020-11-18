# Generated by Django 3.1.2 on 2020-11-18 15:08

import authen.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', authen.models.CustomUserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='student',
            name='profile_picture',
            field=models.ImageField(blank=True, default=None, upload_to='Images/Students'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='profile_picture',
            field=models.ImageField(blank=True, default=None, upload_to='Images/Teachers'),
        ),
        migrations.AlterField(
            model_name='user',
            name='dept',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='jis_ID',
            field=models.CharField(default=None, max_length=20, unique=True),
        ),
    ]
