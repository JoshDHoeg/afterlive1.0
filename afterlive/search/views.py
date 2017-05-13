from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render
from home.models import *
from functools import reduce
from operator import and_, or_


def content_search(request):
    f_list = Festival.objects.all().order_by('?')
    a_list = Artist.objects.all().order_by('?')
    p_list = Photographer.objects.all().order_by('?')
    highlight_list = Content.objects.filter(content_festival = 6)[:16]


    query = request.GET.get("q")
    if query:
        f_list = f_list.filter(name__icontains=query)
        a_list = a_list.filter(name__icontains=query)
        p_list = p_list.filter(name__icontains=query)

    # paginator = Paginator(queryset_list, 6)
    # page = request.GET.get('page')
    # try:
    #     queryset = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     queryset = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     queryset = paginator.page(paginator.num_pages)
    f_list = f_list[:16]
    a_list = a_list[:16]
    p_list = p_list[:16]
    context= {
    "festival_list": f_list,
    "artist_list": a_list,
    "photographer_list": p_list,
    "highlight_list": highlight_list,
    "title": "List"
    }

    return render(request, "search/search.html", context)
