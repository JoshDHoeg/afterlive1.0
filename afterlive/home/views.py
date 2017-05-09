from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render
from home.models import *
from functools import reduce
from operator import and_, or_


def main_page(request):
    highlight_list = Content.objects.filter(content_festival = 6)[:16]

    context= {
        "highlight_list": highlight_list,
    }

    return render(request, "home/main.html", context)
