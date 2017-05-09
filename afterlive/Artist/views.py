from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from home.models import *

def artist_view(request, Experiences_name=None):
    a = Artist.objects.get(name = Experiences_name)
    a_id = a.artist_id
    content_list = Content.objects.filter(content_artist = a_id).order_by('?')

    festival_list = Festival_Artist.objects.filter(a = a_id).order_by('a')
    photographer_list = Photographer_Artist.objects.filter(a = a_id).order_by('a')

    culture_list = Culture.objects.raw('select distinct Culture.Culture_ID, culture.Tag from Culture join Content WHERE Culture.Culture_ID = Content.Content_Culture_ID AND Content.Content_Artist_ID = %s', [a_id])
    type_list = Type.objects.raw('select distinct Type.Type_ID, Type.Content_Type from Type join Content WHERE Type.Type_ID = Content.Content_Type_ID AND Content.Content_Artist_ID = %s', [a_id])


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
        "f": a,
        "content_list": c_list,
        "festival_list": festival_list,
        "type_list": type_list,
        "photographer_list": photographer_list
    }

    return render(request,  'artist/artist.html', context)

def festival_filter_view(request, Experiences_name=None, Detail_name=None):
    a = Artist.objects.get(name = Experiences_name)
    a_id = a.artist_id
    f = Festival.objects.get(name = Detail_name)
    f_id = f.festival_id
    content_list = Content.objects.filter(content_artist = a_id).filter(content_festival = f_id).order_by('?')

    festival_list = Festival_Artist.objects.filter(a = a_id).order_by('a')
    photographer_list = Photographer_Artist.objects.filter(a = a_id).order_by('a')

    type_list = Type.objects.raw('select distinct Type.Type_ID, Type.Content_Type from Type join Content WHERE Type.Type_ID = Content.Content_Type_ID AND Content.Content_Artist_ID = %s', [a_id])

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
        "f": a,
        "content_list": c_list,
        "festival_list": festival_list,
        "type_list": type_list,
        "photographer_list": photographer_list
    }

    return render(request,  'artist/artist.html', context)

def type_filter_view(request, Experiences_name=None, Detail_name=None):

    a = Artist.objects.get(name = Experiences_name)
    a_id = a.artist_id
    t = Type.objects.get(content_type = Detail_name)
    t_id = t.culture_id
    content_list = Content.objects.filter(content_artist = a_id).filter(content_type = t_id).order_by('?')

    festival_list = Festival_Artist.objects.filter(a = a_id).order_by('a')
    photographer_list = Photographer_Artist.objects.filter(a = a_id).order_by('a')

    type_list = Type.objects.raw('select distinct Type.Type_ID, Type.Content_Type from Type join Content WHERE Type.Type_ID = Content.Content_Type_ID AND Content.Content_Artist_ID = %s', [a_id])

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
        "f": a,
        "content_list": c_list,
        "festival_list": festival_list,
        "type_list": type_list,
        "photographer_list": photographer_list
    }

    return render(request,  'artist/artist.html', context)

def photographer_filter_view(request, Experiences_name=None, Detail_name=None):

    a = Artist.objects.get(name = Experiences_name)
    a_id = a.artist_id
    p = Photographer.objects.get(name = Detail_name)
    p_id = t.culture_id
    content_list = Content.objects.filter(content_artist = a_id).filter(content_photographer = p_id).order_by('?')

    festival_list = Festival_Artist.objects.filter(a = a_id).order_by('a')
    photographer_list = Photographer_Artist.objects.filter(a = a_id).order_by('a')

    type_list = Type.objects.raw('select distinct Type.Type_ID, Type.Content_Type from Type join Content WHERE Type.Type_ID = Content.Content_Type_ID AND Content.Content_Artist_ID = %s', [a_id])

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
        "f": a,
        "content_list": c_list,
        "festival_list": festival_list,
        "type_list": type_list,
        "photographer_list": photographer_list
    }


    return render(request,  'artist/artist.html', context)
