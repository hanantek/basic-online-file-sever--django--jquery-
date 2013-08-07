# -*- coding: utf-8 -*-
# 
#  urls.py
#  cloud
#  
#  Created by Daniel Vasquez C. on 2013-05-24.
#  url dispatcher for all app
# 

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from views import *

from cloud.facebook import facebook_view

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),
    url(r'^home', HomeView.as_view()),
    url(r'', include('social_auth.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),    
    url(r'^files/', include('filebrowser.urls')),
    url(r'^player/', include('player.urls')),
    url(r'^gallery/', include('gallery.urls')),
) 

if settings.DEBUG:
    urlpatterns += patterns('',
            url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
            url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
    )
    
