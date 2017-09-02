from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^terms/', include('terms.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^artist/', include('Artist.urls')),
    url(r'^festival/', include('Festival.urls')),
    url(r'^photographer/', include('Photographer.urls')),
]
