"""smilefeet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from smilefeet import views, settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', include(views.home), name='home'),
    url(r'^$', views.home, name='home'),
    url(r'^page2$', views.page2, name='page2'),
    url(r'^page3$', views.page3, name='page3'),
    url(r'^page4$', views.page4, name='page4'),
    url(r'^upload$', views.upload, name='upload'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
