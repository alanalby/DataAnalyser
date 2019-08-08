from rest_framework import serializers
from subscription.models import *
from product.models import *



class S3PortaldataUsageSerializer(serializers.ModelSerializer):	
	message = serializers.SerializerMethodField()

	def get_message(self, data):
		return data['message']

	class Meta:
		model = S3DataUsage
		fields = [
        	'id',
        	'portal_name',
            'total_data_upload',
            'total_data_download',
            'to_date',
            'message',
        ]

