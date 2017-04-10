# from django.views.generic import ListView
# from home.models import *
# from functools import reduce
# from operator import and_, or_
#
# class home_view(ListView):
#     model = Festival
#     template_name = "home/main.html"


    # def get_context_data(self, **kwargs):
    #     context = super(home_view, self).get_context_data(**kwargs)
    #     context['festival_list'] = Festival.objects.all().select_related("LinkID")
    #     context['photographer_list'] = Photographer.objects.all().select_related("LinkID")
    #     context['highlight_list'] = Content.objects.filter(ContentType="Highlight")
    #     return context
