# Generated by Django 3.1.5 on 2021-03-22 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210323_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='sell',
            name='timestamp',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
