from django.http import HttpResponse
from django.shortcuts import render
from .models import SquirrelTracker
import random
# Create your views here.

def map(request):
    sightingList = random.sample(list(SquirrelTracker.objects.all()),100)
    sightings = []
    for sighting in sightingList:
        sightings.append({'latitude':sighting.Y, 'longitude': sighting.X})
    context = {'sightings':sightings,}
    
    return render(request, 'map/map.html', context)
