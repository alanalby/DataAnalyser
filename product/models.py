from django.db import models
from django.utils import timezone

# Create your models here.

class S3DataUsage(models.Model):
	portal_name = models.CharField(max_length=255, null=False)
	total_data_upload = models.BigIntegerField(blank=True, default=0)
	total_data_download = models.BigIntegerField(blank=True, default=0)
	from_date = models.DateTimeField(null=False, blank=False)
	to_date = models.DateTimeField(null=False, blank=False)
	modified_tme = models.DateTimeField(null=True, blank=True,default = timezone.now)

	def __str__(self):
		return "{} - {}".format(self.portal_name, self.from_date, self.to_date)

	class Meta:
		indexes = [
			models.Index(fields=['portal_name']),
			models.Index(fields=['from_date']),
			models.Index(fields=['to_date'])
		]