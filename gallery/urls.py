# -*- coding: utf-8 -*-
# 
#  urls.py
#  cloud
#  
#  Created by Daniel Vasquez C. on 2013-05-31.
#  Url dispatcher for gallery
# 

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from views import *

urlpatterns = patterns('',
   url(r'^$', GalleryView.as_view(), name='gallery'),
)