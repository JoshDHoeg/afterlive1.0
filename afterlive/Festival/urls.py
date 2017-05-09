from django.conf.urls import url, include
from django.views.generic import TemplateView
from Festival.views import *

urlpatterns = [
    url(r'^$', festival_view),
    url(r'^(?P<Experiences_name>[\w\s]+)/$', festival_view),
    url(r'^(?P<Experiences_name>[\w\s]+)/Artist/(?P<Detail_name>[\w\s]+)/$', artist_filter_view),
    url(r'^(?P<Experiences_name>[\w\s]+)/Culture/(?P<Detail_name>[\w\s]+)/$', culture_filter_view),
    url(r'^(?P<Experiences_name>[\w\s]+)/Type/(?P<Detail_name>[\w\s]+)/$', type_filter_view),
    url(r'^(?P<Experiences_name>[\w\s]+)/Photographer/(?P<Detail_name>[\w\s]+)/$', photographer_filter_view),
]
