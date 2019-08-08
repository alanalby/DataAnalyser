from django.db import models
from django.utils import timezone
# Create your models here.


class S3Files(models.Model):
	file_name = models.CharField(max_length=255, null=False)
	created_date = models.DateTimeField(null=True, blank=True,default = timezone.now)
