from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from home.models import Link
from . import views

urlpatterns = [
    url(r'^$', views.content_search)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

print urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
