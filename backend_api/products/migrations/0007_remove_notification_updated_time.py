# Generated by Django 2.2.4 on 2019-08-18 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_notification_seen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='updated_time',
        ),
    ]