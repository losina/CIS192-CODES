# Generated by Django 2.2.7 on 2019-12-10 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20191210_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='category',
            field=models.ForeignKey(default='c', on_delete=django.db.models.deletion.CASCADE, to='core.Category'),
            preserve_default=False,
        ),
    ]
