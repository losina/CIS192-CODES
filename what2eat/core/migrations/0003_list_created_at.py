# Generated by Django 2.2.7 on 2019-12-10 19:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191210_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
