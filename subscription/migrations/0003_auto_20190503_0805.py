# Generated by Django 2.2 on 2019-05-03 08:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0002_auto_20190502_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portaldetails',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 3, 8, 5, 27, 920210, tzinfo=utc)),
        ),
    ]
