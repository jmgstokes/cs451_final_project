from django.shortcuts import render

# generic views - see more at https://docs.djangoproject.com/en/2.1/ref/class-based-views/
from django.views import generic

from geopy.distance import distance
from geopy.geocoders import Nominatim

from .forms import LookupForm

from .models import Job

NMHU = [float(35.593553),float(105.2212999)]

class HomeView(generic.TemplateView):
    template_name = 'index.html'


class JobView(generic.DetailView):
    model = Job
    template_name = 'job.html'

    def get_context_data(self, **kwargs):
        context = super(JobView, self).get_context_data(**kwargs) 
        try:
            q = self.request.GET['location']
        except:
            pass
        return context

class JobListView(generic.ListView):
    model = Job
    template_name = 'job_list.html'

class MapView(generic.TemplateView):
    template_name = 'map.html'