"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django.contrib.contenttypes.models import ContentType
from datetime import datetime
from app.models import Page, Section

def home(request):
    """
    Renders the home page. Deprecated static implementation.
    """
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def home_dynamic(request):
    """
    Renders home page dynamically from the database entries
    """

    #FIX: fetch based on page name
    page = Page.objects.get(id=1)
    sections = Section.objects.filter(page=page)

    return render(
        request, 
        'app/home.html',
        context_instance = RequestContext(request,
        {
            'page': page,
            'year':datetime.now().year,
        })
     )
            
