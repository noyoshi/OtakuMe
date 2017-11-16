# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.conf import settings

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'project/home.html')
