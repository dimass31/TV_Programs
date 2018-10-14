from django.contrib import admin
from django.conf.urls import url
from django.urls import path

from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.search_form, name='search_form'),
    url(r'^search/$', views.search, name='search'),
]
