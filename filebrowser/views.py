# -*- coding: utf-8 -*-
# 
#  views.py
#  cloud
#  
#  Created by Daniel Vasquez C. on 2013-05-22.
#  class view for display data in templates
# 

from django.views.generic.list import ListView
from django.http import HttpResponse
from forms import FileUploadForm
from forms import SearchForm
from filebrowser.models import File

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

class SearchView(ListView):
    template_name = 'search/search.html'
    context_object_name = 'results'
    
    def get_queryset(self):
        form = SearchForm(self.request.GET)
        if form.is_valid():
            return File.objects.filter(name__icontains=form.cleaned_data['name'])
        else:
            return File.objects.all()
                
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(SearchView, self).get_context_data(**kwargs)
        return context


def list(request):
    # Handle file upload
    form = FileUploadForm(request.POST or None, request.FILES)
    if form.is_valid():
        for obj_file in request.FILES.getlist('file'):
            fileup = File(file = obj_file)
            fileup.save()
        # Redirect to the search view after POST
        return HttpResponseRedirect(reverse('files'))
    results = File.objects.all()
    
    return render_to_response(
        'search/search.html',
        {'results': results, 'form': form},
        context_instance = RequestContext(request)
    )