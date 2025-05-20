from django.urls import path,include
"from django.conf.urls import url"
from django.urls import re_path, path
from home.views import *
from car_dealer_portal import *
from customer_portal import *

urlpatterns = [
    re_path(r'^$',home_page),
]
