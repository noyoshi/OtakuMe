# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.conf import settings

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from get_info import get_anime_info

def index(request):
    return render(request, 'project/home.html')

def anime(request):
    description = {}
    search = request.GET.get('search')
    if search==None:
        print "BAD SEARCH AGAIN"
        return render_to_response('project/anime.html', {'descriptions': descriptions})
    print search
    descriptions = get_anime_info(search)
    print "derp"
    return render_to_response('project/anime.html', {'descriptions': descriptions})
