# Generated by Django 2.2 on 2019-05-16 04:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0005_auto_20190515_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='portaldetails',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 16, 4, 57, 48, 118514, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='portaldetails',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]