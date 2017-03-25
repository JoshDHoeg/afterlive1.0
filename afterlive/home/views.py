from django.views.generic import ListView
from home.models import *
from functools import reduce
from operator import and_, or_

class home_view(ListView):
    model = Festival
    template_name = "home/home.html"


    def get_context_data(self, **kwargs):
        context = super(home_view, self).get_context_data(**kwargs)
        context['festival_list'] = Festival.objects.all().select_related("LinkID")
        return context

    def get_context_data(self, **kwargs):
        context = super(home_view, self).get_context_data(**kwargs)
        context['photographer_list'] = Photographer.objects.all().select_related("LinkID")
        return context
