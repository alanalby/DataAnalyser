from django.shortcuts import render
from django.conf import settings

from s3.models import *
from product.models import *
from django.conf import settings
from django.http import HttpResponse

import psycopg2
import boto
import glob
import os
import gzip
import json
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view


class DataBandwidthCalculation:
	def __init__(self,file_name):
		self.file = open(file_name,'rb')
		self.portal_data = {}
		self.file_name = file_name
	def file_filtering(self):
		try:
			self.config = json.load(  gzip.GzipFile(fileobj=self.file, mode='rb') )
			self.list =  np.asarray( self.config['Records'] )
			# print(self.list)
			for events in self.list:
				if 'requestParameters' in events and events['requestParameters'] and 'key' in events['requestParameters']:
					key_list = np.asarray( events['requestParameters']['key'].split ('/') )
					if key_list.size > 0 and key_list[0] not in self.portal_data:
						self.portal_data[key_list[0] ] =  {'total_data_upload':0 ,'total_data_download':0 }
					self.portal_data[key_list[0]]['total_data_upload'] = self.portal_data[key_list[0]]['total_data_upload'] + events['additionalEventData']['bytesTransferredIn']
					self.portal_data[key_list[0]]['total_data_download'] = self.portal_data[key_list[0]]['total_data_download'] + events['additionalEventData']['bytesTransferredOut']
					self.portal_data[key_list[0]]['from_date'] = events['eventTime']
		except:
			print("An exception occurred during executing the file",self.file_name)
			pass

	def final_data(self):
		for portal_name,portal in self.portal_data.items():
			print(portal_name,":::  portal_name")
			if not portal_name == 'common_certificates_of_portal':
				S3DataUsage.objects.create(portal_name=portal_name,
										total_data_upload=portal['total_data_upload'],
										total_data_download=portal['total_data_download'],
										from_date=portal['from_date'],
										to_date=portal['from_date'],
										)


def process_data(filename):
	# file_name_list.append(file_name)
	file_obj = DataBandwidthCalculation('/tmp/'+filename)
	file_obj.file_filtering()
	file_obj.final_data()

def filedownload_thread(object,filename):
	object.get_contents_to_filename('/tmp/'+filename)
	process_data(filename)
	S3Files.objects.create(file_name=filename)

def downloads3files(file_name_list):
	conn = boto.s3.connect_to_region(aws_access_key_id = settings.AWS_ACCESS_KEY_ID,aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY,region_name=settings.REGION)
	bucket = conn.lookup(settings.BUCKET)
	prefix = 'AWSLogs/#####/CloudTrail/eu-central-1/'
	executor = ThreadPoolExecutor(max_workers=10)
	for object in bucket.list(prefix=prefix):
		key_list = object.key.split ('/')
		if key_list[-1] in file_name_list:
			continue
		task1 = executor.submit(filedownload_thread(object,key_list[-1]))
	return

@api_view(['GET', ])
def gets3logs(request):
	if request.user.is_authenticated:
		file_name_list = list(S3Files.objects.values_list('file_name'))
		permission_classes = (IsAuthenticated,) 
		downloads3files(file_name_list)
	else:
		raise APIException("Authentication failed")
	# path = '/tmp'
	# for filepath in glob.glob(os.path.join(path, '*.gz')):
	# 	print(filepath)
	# 	file_name = filepath.split ('/')[-1]
	# 	if file_name in file_name_list:
	# 		continue
	# 	file_name_list.append(file_name)
	# 	file_obj = DataBandwidthCalculation(filepath)
	# 	file_obj.file_filtering()
	# 	file_obj.final_data()

	return HttpResponse({})



