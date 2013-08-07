# -*- coding: utf-8 -*-
# 
#  views.py
#  cloud
#  
#  Created by Daniel Vasquez C. on 2013-05-29.
#  All views for player music
# 

from django.views.generic.base import TemplateView

class PlayerView(TemplateView):
    template_name = 'player/index.html'

    def get_context_data(self, **kwargs):
        player = None
        return {'player': player}
