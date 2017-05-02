from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from home.models import *

def festival_view(request, Experiences_name=None):
    a_list = Festival.objects.get(name = Experiences_name)
    content_list = Content.objects.filter(content_festival = a_list.festival_id)

    artist_list = Festival_Artist.objects.filter(fl = a_list.festival_id).order_by('a')
    photographer_list = Festival_Photographer.objects.filter(festival_festival = a_list.festival_id)

    paginator = Paginator(content_list, 12)
    page = request.GET.get('page')
    try:
        c_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        c_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        c_list = paginator.page(paginator.num_pages)

    context = {
        "title" : "dude",
        "a" : a_list,
        "content_list": c_list,
        "artist_list": artist_list
    }

    return render(request,  'festival/festival.html', context)
