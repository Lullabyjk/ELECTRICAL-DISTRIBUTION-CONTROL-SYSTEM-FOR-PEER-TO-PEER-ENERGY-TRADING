# Generated by Django 3.1.5 on 2021-03-24 14:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_rpcconfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpcconfig',
            name='rpc_host',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
