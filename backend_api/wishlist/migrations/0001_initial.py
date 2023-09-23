# Generated by Django 2.2.4 on 2019-08-18 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapping_id', models.IntegerField(default=0)),
                ('brand', models.CharField(max_length=50)),
                ('description', djongo.models.fields.ListField(verbose_name=models.CharField(max_length=500))),
                ('display_size', models.CharField(max_length=10)),
                ('graphics_memory', models.CharField(max_length=30)),
                ('img_link', models.URLField(max_length=10000)),
                ('product_title', models.CharField(max_length=1000)),
                ('ram', models.CharField(max_length=10)),
                ('ram_type', models.CharField(max_length=100)),
                ('storage', djongo.models.fields.DictField()),
                ('websites', djongo.models.fields.ListField(verbose_name=djongo.models.fields.EmbeddedModelField(model_container=products.models.Website, null=True))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]