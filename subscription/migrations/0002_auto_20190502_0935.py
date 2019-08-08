# Generated by Django 2.2 on 2019-05-02 09:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portaldetails',
            name='access_key',
        ),
        migrations.AddField(
            model_name='portaldetails',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 2, 9, 35, 7, 979281, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='portaldetails',
            name='date_purged',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portaldetails',
            name='expire_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portaldetails',
            name='is_trial',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='portaldetails',
            name='plan_id',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='portaldetails',
            name='subscription_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='portaldetails',
            name='updated_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='portaldetails',
            name='portal_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
