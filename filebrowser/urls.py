# -*- coding: utf-8 -*-
# 
#  url.py
#  cloud
#  
#  Created by Daniel Vasquez C. on 2013-05-21.
#  Url dispatcher for files app
# 

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from views import SearchView, list


urlpatterns = patterns('',
   url(r'^$', SearchView.as_view(), name='files'),
   url(r'^upload/$', 'filebrowser.views.list', name='upload' ), 
)