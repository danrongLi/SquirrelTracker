from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from SquirrelFinder import views
from django.urls import path

urlpatterns = [ 
    url(r'', views.map, name="map"),
    path('index/',views.index),
]
