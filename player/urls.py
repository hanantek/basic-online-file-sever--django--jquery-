# -*- coding: utf-8 -*-
# 
#  urls.py
#  cloud
#  
#  Created by Daniel Vasquez C. on 2013-05-29.
#  Route manager for player app
# 

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from views import *

urlpatterns = patterns('',
   url(r'^$', PlayerView.as_view(), name='player'),
)