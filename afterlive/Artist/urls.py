"""afterlive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic import TemplateView
# from home.models import Link
from Artist.views import *

urlpatterns = [
    url(r'^$', artist_view),
    url(r'^(?P<Experiences_name>[\w\s]+)/$', artist_view),
    url(r'^(?P<Experiences_name>[\w\s]+)/Festival/(?P<Detail_name>[\w\s]+)/$', festival_filter_view),
    url(r'^(?P<Experiences_name>[\w\s]+)/Type/(?P<Detail_name>[\w\s]+)/$', type_filter_view),
    url(r'^(?P<Experiences_name>[\w\s]+)/Photographer/(?P<Detail_name>[\w\s]+)/$', photographer_filter_view),
]
