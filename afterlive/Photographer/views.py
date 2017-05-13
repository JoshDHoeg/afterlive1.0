from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from home.models import *

def photographer_view(request, Experiences_name=None):
    p = Photographer.objects.get(name = Experiences_name)
    p_id = p.photographer_id
    content_list = Content.objects.filter(content_photographer = p_id).order_by('?')

    artist_list = Photographer_Artist.objects.filter(p = p_id).order_by('a')
    festival_list = Festival_Photographer.objects.filter(photographer_photographer = p_id)

    type_list = Type.objects.raw('select distinct type.Type_ID, type.Content_Type from type join content WHERE type.Type_ID = content.Content_Type_ID AND content.Content_Photographer_ID = %s', [p_id])


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
        "f": p,
        "content_list": c_list,
        "artist_list": artist_list,
        "type_list": type_list,
        "festival_list": festival_list
    }

    return render(request,  'photographer/photographer.html', context)

def artist_filter_view(request, Experiences_name=None, Detail_name=None):
    p = Photographer.objects.get(name = Experiences_name)
    p_id = p.photographer_id
    a = Artist.objects.get(name = Detail_name)
    a_id = a.artist_id
    content_list = Content.objects.filter(content_photographer = p_id).filter(content_artist = a_id).order_by('?')

    artist_list = Photographer_Artist.objects.filter(p = p_id).order_by('a')
    festival_list = Festival_Photographer.objects.filter(photographer_photographer = p_id)

    type_list = Type.objects.raw('select distinct type.Type_ID, type.Content_Type from type join content WHERE type.Type_ID = content.Content_Type_ID AND content.Content_Photographer_ID = %s', [p_id])


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
        "f": p,
        "content_list": c_list,
        "artist_list": artist_list,
        "type_list": type_list,
        "festival_list": festival_list
    }

    return render(request,  'photographer/photographer.html', context)


def type_filter_view(request, Experiences_name=None, Detail_name=None):
    p = Photographer.objects.get(name = Experiences_name)
    p_id = p.photographer_id
    t = Type.objects.get(content_type = Detail_name)
    t_id = t.type_id
    content_list = Content.objects.filter(content_photographer = p_id).filter(content_type = t_id).order_by('?')

    artist_list = Photographer_Artist.objects.filter(p = p_id).order_by('a')
    festival_list = Festival_Photographer.objects.filter(photographer_photographer = p_id)

    type_list = Type.objects.raw('select distinct type.Type_ID, type.Content_Type from type join content WHERE type.Type_ID = content.Content_Type_ID AND content.Content_Photographer_ID = %s', [p_id])


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
        "f": p,
        "content_list": c_list,
        "artist_list": artist_list,
        "type_list": type_list,
        "festival_list": festival_list
    }

    return render(request,  'photographer/photographer.html', context)

def festival_filter_view(request, Experiences_name=None, Detail_name=None):
    p = Photographer.objects.get(name = Experiences_name)
    p_id = p.photographer_id
    f = Festival.objects.get(name = Detail_name)
    f_id = f.festival_id
    content_list = Content.objects.filter(content_photographer = p_id).filter(content_festival = f_id).order_by('?')

    artist_list = Photographer_Artist.objects.filter(p = p_id).order_by('a')
    festival_list = Festival_Photographer.objects.filter(photographer_photographer = p_id)

    type_list = Type.objects.raw('select distinct type.Type_ID, type.Content_Type from type join content WHERE type.Type_ID = content.Content_Type_ID AND content.Content_Photographer_ID = %s', [p_id])



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
        "f": p,
        "content_list": c_list,
        "artist_list": artist_list,
        "type_list": type_list,
        "festival_list": festival_list
    }

    return render(request,  'photographer/photographer.html', context)
