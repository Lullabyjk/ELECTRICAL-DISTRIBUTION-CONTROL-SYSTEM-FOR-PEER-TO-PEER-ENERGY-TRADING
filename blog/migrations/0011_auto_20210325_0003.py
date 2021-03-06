# Generated by Django 3.1.5 on 2021-03-24 17:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_rpcconfig_rpc_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='blob',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='history',
            name='status',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
