from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import *
from .serializers import *
from django.utils import timezone
# tests for views


class BaseViewTest(APITestCase):
	client = APIClient()

	@staticmethod
	def create_song(portal_name="", total_data_upload="",total_data_download="",from_date="",to_date=""):
		print("Creating DAtabase")
		S3DataUsage.objects.create(title=title, artist=artist)

	def setUp(self):
        # add test data
		self.create_song("Support-demo", 10,10,timezone.now,timezone.now)
		self.create_song("Support-demo1", 20,20,timezone.now,timezone.now)
		self.create_song("Support-demo2", 30,30,timezone.now,timezone.now)
		self.create_song("Support-demo3", 40,40,timezone.now,timezone.now)
		self.create_song("Support-demo4", 50,50,timezone.now,timezone.now)
        