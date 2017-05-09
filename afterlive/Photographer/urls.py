from django.conf.urls import url, include
from django.views.generic import TemplateView
from Photographer.views import *

urlpatterns = [
    url(r'^$', photographer_view),
    url(r'^(?P<Experiences_name>[\w\s]+)/$', photographer_view),
        url(r'^(?P<Experiences_name>[\w\s]+)/Artist/(?P<Detail_name>[\w\s]+)/$', artist_filter_view),
        url(r'^(?P<Experiences_name>[\w\s]+)/Type/(?P<Detail_name>[\w\s]+)/$', type_filter_view),
        url(r'^(?P<Experiences_name>[\w\s]+)/Festival/(?P<Detail_name>[\w\s]+)/$', festival_filter_view),
]
