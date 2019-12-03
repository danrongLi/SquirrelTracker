from django.conf.urls import url                                                                                                                              
from SquirrelFinder import views

urlpatterns = [ 
    url(r'', views.map, name="map"),
]
