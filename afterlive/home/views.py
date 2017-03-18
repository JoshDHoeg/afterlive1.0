from django.views.generic import ListView
from home.models import *
from functools import reduce
from operator import and_, or_

class festival_view(ListView):
    model = Festival
    template_name = "home/home.html"


    def get_context_data(self, **kwargs):
        context = super(festival_view, self).get_context_data(**kwargs)
        context['festival_list'] = Festival.objects.all().select_related("LinkID")
        return context
