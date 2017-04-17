from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse
from home.models import *

def artist_view(request, Experiences_name=None):
    a_list = Artist.objects.get(Name = Experiences_name)
    content_list = Content.objects.all()

    paginator = Paginator(content_list, 6)
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
        "content_list": c_list
    }
    return render(request,  'artist/artist.html', context)
