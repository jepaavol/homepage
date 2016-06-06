"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django.contrib.contenttypes.models import ContentType

from rest_framework import viewsets

from datetime import datetime
from app.models import Page, Section, Image, ImageBar, Paragraph
from app.serializers import PageSerializer, ImageSerializer, ImageBarSerializer, SectionSerializer, ParagraphSerializer


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
            

class PageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageBarViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ImageBar.objects.all()
    serializer_class = ImageBarSerializer


class SectionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class ParagraphViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer