# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.conf import settings

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from get_info import get_anime_info, get_manga_info

def index(request):
    return render(request, 'project/home.html')

def anime(request):
    descriptions = {}
    search = request.GET.get('search')
    if search==None:
        print "BAD SEARCH AGAIN"
        return render_to_response('project/results.html', {'descriptions': descriptions})
    print search
    anime_descriptions = get_anime_info(search)
    manga_descriptions = get_manga_info(search)


    print "derp"
    return render_to_response('project/results.html', {'manga_descriptions': manga_descriptions, 'anime_descriptions': anime_descriptions})

    # return render_to_response('project/anime.html', {'descriptions': descriptions})

def manga(request):
    pass
