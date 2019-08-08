from django.urls import path
from .views import *


urlpatterns = [
    path('updatedatausage/', gets3logs, name="gets3log"),
 ]