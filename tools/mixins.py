# -*- coding: utf-8 -*-
# 
#  models.py
#  cloud
#  
#  Created by Daniel Vasquez C. on 2013-05-21.
#  Mixin class for all models
#

from django.db import models

class TrackingMixin(models.Model):
    
    created = models.DateTimeField('created', auto_now_add = True)
    modified = models.DateTimeField('modified', auto_now = True)
    
    class Meta:
        abstract = True