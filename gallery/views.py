# Create your views here.

from django.views.generic import TemplateView
from filebrowser.models import File

class GalleryView(TemplateView):
    template_name = "gallery/gallery.html"
    
    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        context['list_images'] = File.objects.filter(content_type__regex=r'image').order_by('-modified')
        return context
