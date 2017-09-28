# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-28 13:41
from __future__ import unicode_literals

import Catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0006_auto_20170928_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pictureUrl',
            field=models.ImageField(blank=True, null=True, upload_to=Catalog.models.get_product_image_path),
        ),
    ]
