# -*- coding: utf-8 -*-
# 
#  admin.py
#  cloud
#  
#  Created by Daniel Vasquez C. on 2013-05-21.
#  admin module for filebrowser models
# 

from django.contrib import admin
from models import File

class FileAdmin(admin.ModelAdmin):
    pass

admin.site.register(File, FileAdmin)