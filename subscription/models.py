from django.db import models
from django.utils import timezone
# Create your models here.

class PortalDetails(models.Model):
	portal_name = models.CharField(max_length=255, null=False,unique=True)
	total_device = models.IntegerField(blank=True, default=0)
	data_allowed = models.BigIntegerField(blank=True, default=250)
	plan_id = models.IntegerField(blank=True, default=0)
	expire_date = models.DateTimeField(null=True, blank=True)
	created_date = models.DateTimeField(null=True, blank=True)
	updated_date = models.DateTimeField(null=True, blank=True)
	date_purged = models.DateTimeField(null=True, blank=True)
	is_trial = models.BooleanField(default=False)
	subscription_status = models.IntegerField(default=0) #0. trail, 1: active, 2: past due 3: unpaid, 4: expired, 5:trail end, 6. cancelled
	modified_date = models.DateTimeField(default=timezone.now())