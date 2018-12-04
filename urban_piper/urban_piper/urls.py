"""urban_piper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from delivery import views

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    # url(r"^accounts/", views.login),
    url(r"^$", views.index),
    url(r"^login$", views.login),
    url(r"^logout$", views.logout),
    url(r"^dashboard$", views.dashboard),
    url(r"^dashboard/$", views.dashboard),
    url(r"^dashboard/task$", views.task),
    url(r"^dashboard/task/$", views.task),
    url(r"^dashboard/task/new$", views.newtask),
    url(r"^dashboard/task/(?P<id>\d+)/cancel$", views.canceltask),
    url(r"^dashboard/delivery_task$", views.deliverytask),
    url(r"^dashboard/delivery_task/$", views.deliverytask),
    url(r"^dashboard/delivery_task/(?P<id>\d+)/complete$", views.completetask),
    url(r"^dashboard/delivery_task/(?P<id>\d+)/decline$", views.declinetask),
    url(r"^dashboard/delivery_task/(?P<id>\d+)/accept$", views.accepttask),
    url(r"^send_message$", views.send_message),
    url(r"^receive_message$", views.receive_message),
]

