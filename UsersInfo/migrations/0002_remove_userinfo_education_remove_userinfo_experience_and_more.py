# Generated by Django 4.1 on 2022-08-17 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsersInfo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='Education',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='Experience',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='Profession',
        ),
        migrations.AddField(
            model_name='education',
            name='Lang',
            field=models.CharField(default='en', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experience',
            name='Lang',
            field=models.CharField(default='en', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qualification',
            name='Lang',
            field=models.CharField(default='en', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='Lang',
            field=models.CharField(default='en', max_length=20),
            preserve_default=False,
        ),
    ]
