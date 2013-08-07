# -*- coding: utf-8 -*-
# 
#  models.py
#  cloud
#  
#  Created by Daniel Vasquez C. on 2013-05-21.
#  file model for storing uploaded files from users
# 
import os
import uuid

from datetime import date, datetime
from django.conf import settings
from django.db import models
from tools.mixins import TrackingMixin

# Rename files at uploaded use UUID for unique names
def update_filename(instance, filename):
    today = datetime.now()
    today_path = today.strftime("%Y/%m/%d")
    path = "files/"
    ext = filename.split('.')[-1]
    #instance.transaction_uuid + instance.file_extension
    format = "%s.%s" % (uuid.uuid4(), ext) 
    return os.path.join(today_path, format)
    
def update_thumbnail(instance, filename):
    today = datetime.now()
    today_path = today.strftime("%Y/%m/%d/thumbnail")
    path = "files/"
    ext = filename.split('.')[-1]
    #instance.transaction_uuid + instance.file_extension
    format = "%s.%s" % (uuid.uuid4(), ext) 
    return os.path.join(today_path, format)
    
# Model for file storing
class File(TrackingMixin):
    name = models.CharField(max_length=150, null=True, blank=True)
    file = models.FileField(upload_to = update_filename, null=False, blank=False)
    thumbnail = models.ImageField(upload_to = update_thumbnail, null=True, blank=True)
    content_type = models.CharField(max_length=25)
    #counter = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.name
        
    def create_thumbnail(self):
        
        if not self.file:
            return
        
        from PIL import Image
        from cStringIO import StringIO
        from django.core.files.uploadedfile import SimpleUploadedFile
        import os
        
        # Set our thumbnail size in a tuple (max width, max height)
        THUMBNAIL_SIZE = (200, 200)
        
        FILE_TYPE = self.file.file.content_type

        if FILE_TYPE == 'image/jpeg':
            PIL_TYPE = 'jpeg'
            FILE_EXTENSION = 'jpg'
        elif FILE_TYPE == 'image/png':
            PIL_TYPE = 'png'
            FILE_EXTENSION = 'png'
        else :
            return
        
        # Open original photo which we want to thumbnail using PIL's image    
        image =  Image.open(StringIO(self.file.read()))
        # get size
        xsize, ysize = image.size
        #get minimum size
        minsize = min(xsize, ysize)
        # largest square possible in the image
        xnewsize = (xsize-minsize)/2
        ynewsize = (ysize-minsize)/2
        # crop it
        image2 = image.crop((xnewsize, ynewsize, xsize-xnewsize, ysize-ynewsize))
        # load is necessary after crop
        image2.load()
        # We use our PIL Image object to create the thumbnail
        image2.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
        # Save the thumbnail
        temp_handle = StringIO()
        image2.save(temp_handle, PIL_TYPE)
        temp_handle.seek(0)
        
        suf = SimpleUploadedFile(os.path.split(self.file.name)[-1],
                         temp_handle.read(), content_type=FILE_TYPE)
        # Save SimpleUploadedFile into image field
        self.thumbnail.save('%s_thumbnail.%s'%(os.path.splitext(suf.name)[0],
                            FILE_EXTENSION), suf, save=False)
    
    def save(self):
        print "---> name : %s, content_type : %s" % (self.file.name,str(self.file.file.content_type))
        self.name = self.file.name
        self.content_type = self.file.file.content_type
        self.create_thumbnail()
        super(File, self).save()