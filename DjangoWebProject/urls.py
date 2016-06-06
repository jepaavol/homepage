"""
Definition of urls for DjangoWebProject.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm

from django.conf.urls import include
from django.contrib import admin
from rest_framework import routers

from app import views

admin.autodiscover()

router = routers.DefaultRouter()
router.register(str(views.PageViewSet().serializer_class.Meta.model.__name__).lower(), 
                views.PageViewSet)
router.register(str(views.ImageViewSet().serializer_class.Meta.model.__name__).lower(), 
                views.ImageViewSet)
router.register(str(views.ImageBarViewSet().serializer_class.Meta.model.__name__).lower(), 
                views.ImageBarViewSet)
router.register(str(views.SectionViewSet().serializer_class.Meta.model.__name__).lower(), 
                views.SectionViewSet)
router.register(str(views.ParagraphViewSet().serializer_class.Meta.model.__name__).lower(), 
                views.ParagraphViewSet)


urlpatterns = patterns('',
    # Examples:
    url(r'^old$', views.home),
    url(r'^$', views.home_dynamic),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),


    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)
