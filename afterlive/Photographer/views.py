from django.shortcuts import render
from django.http import HttpResponse
from home.models import *

def photographer_view(request, Experiences_name=None):
    a_list = Photographer.objects.get(Name = Experiences_name)
    context = {
        "title" : "dude",
        "a" : a_list
    }
    return render(request,  'photographer/photographer.html', context)
