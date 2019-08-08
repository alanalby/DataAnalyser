from django.urls import path
from .views import *

urlpatterns = [
    path('listtotaldatausage/', ListTotalDataUsageView.as_view(), name="listalldatausage"),
    path('listtotalportaldatausage/', ListTotalPortalDataUsageView.as_view(), name="listalldatausage"),
    # path('createportal/', PortalCreateView.as_view(), name="createportal"),
    path('updateportal/', PortalUpdateView.as_view( ), name="updateportal"),
    path('create_sample_data/', CreateSampleDataUsageView.as_view(), name="create_sample_data"),

 ]
