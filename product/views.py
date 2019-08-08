from django.shortcuts import render


from rest_framework import generics
# from subscription.serializers import *
from product.serializers import *
from product.models import *
from django.utils import timezone
from rest_framework import serializers
from datetime import datetime
from django.db.models import Avg, Max, Min, Sum
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated

from django.conf import settings
import json
# Create your views here.
class PortalDataUsageView(generics.ListAPIView):
	serializer_class = S3PortaldataUsageSerializer
	permission_classes = (IsAuthenticated,) 
	def get_queryset(self):
		data =  self.request.GET.get('data') 
		data = json.loads(data)
		print(data['portal_name'],data['from_date'],data['to_date'])
		try: 
			final_data = (S3DataUsage.objects.filter(portal_name=data['portal_name'],from_date__gte=data['from_date'],to_date__lte=data['to_date']).values('portal_name').annotate(total_data_upload=Sum('total_data_upload'),total_data_download=Sum('total_data_download'),to_date=Max('to_date')))
			if final_data:
				final_data['message'] = 'success'
				final_data['error_code'] = ''
				response = final_data
			else:
				response = {'portal_name':'','total_data_upload':0,'total_data_download':0,'to_date':data['to_date'],'message': 'no entry found'}
			return [response]
		except Exception as e:
			print('Internal Server Error',e)
			raise APIException("Internal Server Error")
			
