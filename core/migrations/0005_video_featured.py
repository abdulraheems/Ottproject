# Generated by Django 3.2.7 on 2022-09-12 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_video_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
