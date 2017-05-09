from django.conf.urls import url, include
from home.models import Link
from . import views

urlpatterns = [
    url(r'^$', views.content_search)
]
