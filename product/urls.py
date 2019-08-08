from django.urls import path
from .views import *


urlpatterns = [
    path('getportaldatausage/', GetPortalDataUsageView.as_view(), name="portaldatausage"),
 ]