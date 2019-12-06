from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from . import views
from django.urls import path


urlpatterns = [
        path('map/',views.map),
        path('sightings/stats',views.sighting_stats),
        path('sightings/',views.all_sighting),
        path('sightings/add',views.add_sighting,name='add'),
        #path('sightings/<str:Unique_Squirrel_ID>',views.edit_sighting),
        path('sightings/<Unique_Squirrel_ID>',views.edit_sighting,name='edit_sighting'),

]
