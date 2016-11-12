from django.shortcuts import render
from django.http import HttpResponse
from djangoproject.tasks import email
 
def index(request):
    return HttpResponse('This page shows a list of most recent posts.')

import datetime

def firstview(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    email.delay()
    return HttpResponse(html)
