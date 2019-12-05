from django.http import HttpResponse
from django.shortcuts import render
from .models import SquirrelTracker
import random
# Create your views here.

def index(request):
    return HttpResponse('Hi! How are you !!!')

def map(request):
    templist = random.sample(list(SquirrelTracker.objects.all()),100)
    sightings = []
    for temp in templist:
        sightings.append({'latitude':temp.X, 'longitude': temp.Y})
    context = {'sightings':sightings}
    
    return render(request, 'map/map.html', context)
