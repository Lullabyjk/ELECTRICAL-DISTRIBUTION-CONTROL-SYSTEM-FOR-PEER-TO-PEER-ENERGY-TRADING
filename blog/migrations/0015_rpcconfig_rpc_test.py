# Generated by Django 3.2.4 on 2021-06-25 10:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20210624_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpcconfig',
            name='rpc_test',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
