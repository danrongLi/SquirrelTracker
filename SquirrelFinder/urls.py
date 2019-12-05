from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from . import views
from django.urls import path


urlpatterns = [
        path('map/',views.map),
     # path('sightings/', views.all_sightings, name='all_sightings'),
]
