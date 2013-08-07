# -*- coding: utf-8 -*-
# 
#  player.py
#  cloud
#  
#  Created by Daniel Vasquez C. on 2013-05-29.
#  custom template for player
# 

import os
from django import template
from filebrowser.models import File

register = template.Library()

@register.inclusion_tag('player/player.html', takes_context=True)
def playlist(context):
    list = File.objects.filter(file__regex=r'mp3').order_by('-modified')[:10]
    return {'list': list}
