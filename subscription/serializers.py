
from rest_framework import serializers
from .models import *
from product.models import *





class S3PdataUsageSerializer(serializers.ModelSerializer):	
	class Meta:
		model = S3DataUsage
		fields = [
        	'id',
            'portal_name',
            'total_data_upload',
            'total_data_download'
        ]
		lookup_field = 'id'


class PortalCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = PortalDetails
		exclude = ('modified_date',)
		lookup_field = 'portal_name'

class S3dataUsageSerializer(serializers.ModelSerializer):
	class Meta:
		model = S3DataUsage
		fields = '__all__'
		lookup_field = 'id'
		
