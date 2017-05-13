from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from home.models import *

def festival_view(request, Experiences_name=None):
    f = Festival.objects.get(name = Experiences_name)
    f_id = f.festival_id
    content_list = Content.objects.filter(content_festival = f_id).order_by('?')

    artist_list = Festival_Artist.objects.filter(fl = f_id).order_by('a')
    photographer_list = Festival_Photographer.objects.filter(festival_festival = f_id)

    culture_list = Culture.objects.raw('select distinct culture.Culture_ID, culture.Tag from culture join content WHERE culture.Culture_ID = content.Content_Culture_ID AND content.Content_Festival_ID = %s', [f_id])
    type_list = Type.objects.raw('select distinct type.Type_ID, type.Content_Type from type join content WHERE type.Type_ID = content.Content_Type_ID AND content.Content_Festival_ID = %s', [f_id])


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
        "f": f,
        "content_list": c_list,
        "artist_list": artist_list,
        "type_list": type_list,
        "culture_list": culture_list,
        "photographer_list": photographer_list
    }

    return render(request,  'festival/festival.html', context)

def artist_filter_view(request, Experiences_name=None, Detail_name=None):

    f = Festival.objects.get(name = Experiences_name)
    a = Artist.objects.get(name = Detail_name)
    f_id = f.festival_id
    a_id = a.artist_id
    content_list = Content.objects.filter(content_festival = f_id).filter(content_artist = a_id).order_by('?')

    artist_list = Festival_Artist.objects.filter(fl = f_id).order_by('a')
    photographer_list = Festival_Photographer.objects.filter(festival_festival = f_id)

    culture_list = Culture.objects.raw('select distinct culture.Culture_ID, culture.Tag from culture join content WHERE culture.Culture_ID = content.Content_Culture_ID AND content.Content_Festival_ID = %s', [f_id])
    type_list = Type.objects.raw('select distinct type.Type_ID, type.Content_Type from type join content WHERE type.Type_ID = content.Content_Type_ID AND content.Content_Festival_ID = %s', [f_id])


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
        "f": f,
        "a": a.name,
        "content_list": c_list,
        "artist_list": artist_list,
        "type_list": type_list,
        "culture_list": culture_list,
        "photographer_list": photographer_list
    }

    return render(request,  'festival/festival.html', context)


def culture_filter_view(request, Experiences_name=None, Detail_name=None):

    f = Festival.objects.get(name = Experiences_name)
    c = Culture.objects.get(tag = Detail_name)
    f_id = f.festival_id
    c_id = c.culture_id
    content_list = Content.objects.filter(content_festival = f_id).filter(content_culture = c_id).order_by('?')

    artist_list = Festival_Artist.objects.filter(fl = f_id).order_by('a')
    photographer_list = Festival_Photographer.objects.filter(festival_festival = f_id)

    culture_list = Culture.objects.raw('select distinct culture.Culture_ID, culture.Tag from culture join content WHERE culture.Culture_ID = content.Content_Culture_ID AND content.Content_Festival_ID = %s', [f_id])
    type_list = Type.objects.raw('select distinct type.Type_ID, type.Content_Type from type join content WHERE type.Type_ID = content.Content_Type_ID AND content.Content_Festival_ID = %s', [f_id])


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
        "f": f,
        "a": c,
        "content_list": c_list,
        "artist_list": artist_list,
        "type_list": type_list,
        "culture_list": culture_list,
        "photographer_list": photographer_list
    }

    return render(request,  'festival/festival.html', context)

def type_filter_view(request, Experiences_name=None, Detail_name=None):

    f = Festival.objects.get(name = Experiences_name)
    t = Type.objects.get(content_type = Detail_name)
    f_id = f.festival_id
    t_id = t.type_id
    content_list = Content.objects.filter(content_festival = f_id).filter(content_type = t_id).order_by('?')

    artist_list = Festival_Artist.objects.filter(fl = f_id).order_by('a')
    photographer_list = Festival_Photographer.objects.filter(festival_festival = f_id)

    culture_list = Culture.objects.raw('select distinct culture.Culture_ID, culture.Tag from culture join content WHERE culture.Culture_ID = content.Content_Culture_ID AND content.Content_Festival_ID = %s', [f_id])
    type_list = Type.objects.raw('select distinct type.Type_ID, type.Content_Type from type join content WHERE type.Type_ID = content.Content_Type_ID AND content.Content_Festival_ID = %s', [f_id])


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
        "f": f,
        "a": t,
        "content_list": c_list,
        "artist_list": artist_list,
        "type_list": type_list,
        "culture_list": culture_list,
        "photographer_list": photographer_list
    }

    return render(request,  'festival/festival.html', context)

def photographer_filter_view(request, Experiences_name=None, Detail_name=None):

    f = Festival.objects.get(name = Experiences_name)
    p = Photographer.objects.get(name = Detail_name)
    f_id = f.festival_id
    p_id = p.photographer_id
    content_list = Content.objects.filter(content_festival = f_id).filter(content_photographer = p_id).order_by('?')

    artist_list = Festival_Artist.objects.filter(fl = f_id).order_by('a')
    photographer_list = Festival_Photographer.objects.filter(festival_festival = f_id)

    culture_list = Culture.objects.raw('select distinct culture.Culture_ID, culture.Tag from culture join content WHERE culture.Culture_ID = content.Content_Culture_ID AND content.Content_Festival_ID = %s', [f_id])
    type_list = Type.objects.raw('select distinct type.Type_ID, type.Content_Type from type join content WHERE type.Type_ID = content.Content_Type_ID AND content.Content_Festival_ID = %s', [f_id])


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
        "f": f,
        "a": p,
        "content_list": c_list,
        "artist_list": artist_list,
        "type_list": type_list,
        "culture_list": culture_list,
        "photographer_list": photographer_list
    }

    return render(request,  'festival/festival.html', context)
