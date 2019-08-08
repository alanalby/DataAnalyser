from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from subscription.models import *
from subscription.serializers import *
# from product.serializers import *
from product.models import *
from django.utils import timezone
from rest_framework import serializers
from datetime import datetime
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.db.models import Avg, Max, Min, Sum
import random
import string
import json

class ListTotalDataUsageView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = S3DataUsage.objects.all().values('portal_name').annotate(total_data_upload=Sum('total_data_upload'),total_data_download=Sum('total_data_download'))
    serializer_class = S3PdataUsageSerializer
    permission_classes = (IsAuthenticated,)  
        
class ListTotalPortalDataUsageView(generics.ListAPIView):
	serializer_class = S3PdataUsageSerializer
	permission_classes = (IsAuthenticated,)  
	def get_queryset(self):
		data =  self.request.GET.get('data') 
		from_date = self.request.data.get('from_date')
		to_date = self.request.data.get('to_date')
		from_date = datetime.strptime( str(self.request.data.get('from_date') )[1:-1] , "%Y-%m-%d %H:%M:%S")
		to_date = datetime.strptime( str(self.request.data.get('to_date'))[1:-1], "%Y-%m-%d %H:%M:%S")
		return S3DataUsage.objects.filter(from_date__gte=from_date,to_date__lte=to_date).values('portal_name').annotate(total_data_upload=Sum('total_data_upload'),total_data_download=Sum('total_data_download'))
	 

class CreateSampleDataUsageView(generics.CreateAPIView):
	serializer_class = S3dataUsageSerializer
	permission_classes = (IsAuthenticated,)  
	def perform_create(self, serializer):
		serializer.save()

# class PortalCreateView(generics.CreateAPIView):
# 	serializer_class = PortalCreateSerializer
# 	permission_classes = ()
# 	def perform_create(self, serializer):
# 		serializer.save()

class PortalUpdateView(generics.UpdateAPIView):
	serializer_class = PortalCreateSerializer
	permission_classes = (IsAuthenticated,)  
	lookup_fields = ('portal_name')
	def get_object(self,portal_name):
		queryset = PortalDetails.objects.get_or_create(portal_name=portal_name)
		return queryset[0]
	def update(self, request, *args, **kwargs):
		data = request.data
		portal_name = data.get('portal_name', '')
		if not portal_name:
			raise APIException("Portal Name is invalid")
		instance = self.get_object(portal_name)
		serializer = self.get_serializer(instance,data=request.data,partial=True)
		serializer.is_valid()
		response = self.partial_update(serializer)
		return Response()

	def partial_update(self, serializer):
		instance = serializer.save()
		return instance
















	# queryset = PortalDetails.objects.all()
	

	

	# 	if getattr(instance, '_prefetched_objects_cache', None):
	# 		instance._prefetched_objects_cache = {}
	# 	return HttpStreamingResponse(serializer.data)
	# def partial_update(self, request, *args, **kwargs):
	# 	kwargs['partial'] = True
	# 	print(args,"*args")
	# 	print(kwargs,"*kwargs")
	# 	return self.update(request, *args, **kwargs)





