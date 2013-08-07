# -*- coding: utf-8 -*-
# 
#  forms.py
#  cloud
#  
#  Created by Daniel Vasquez C. on 2013-05-22.
#  search form
#  upload and validate form 
# 

from django import forms
from django.conf import settings
from filebrowser.models import File
from django.utils.translation import ugettext_lazy as _

class SearchForm(forms.Form):
    name = forms.CharField(min_length=3, required=False)
    

class FileUploadForm(forms.Form):
    
    file = forms.FileField(
        required=True,
        help_text='max. 50 Mb.'
    )
    
    class Meta:
        model = File
    
    def clean(self):
        if not (self.cleaned_data):
            return None
        content = self.cleaned_data['file']
        #only get type of general content like 'audio' or 'video'        
        content_type = content.content_type.split('/')[0]
        if content_type in settings.CONTENT_TYPES:
            if content.size > settings.MAX_UPLOAD_SIZE:
                raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s')\
                 % (filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content.size)))
        else:
            raise forms.ValidationError(_('File type is not supported'))
        return content