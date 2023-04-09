# Generated by Django 3.2.7 on 2022-09-07 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('channel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='channel',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channel', to=settings.AUTH_USER_MODEL),
        ),
    ]
