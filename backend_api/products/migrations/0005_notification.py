# Generated by Django 2.2.4 on 2019-08-18 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0004_remove_search_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=1000)),
                ('product_link', models.URLField(max_length=1000)),
                ('website_name', models.CharField(max_length=100)),
                ('old_price', models.IntegerField(default=0)),
                ('new_price', models.IntegerField(default=0)),
                ('updated_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
