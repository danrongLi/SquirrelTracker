from django.http import HttpResponse
from django.shortcuts import render
from .models import SquirrelTracker
from .forms import SquirrelForm

import random
# Create your views here.

def map(request):
    sightingList = random.sample(list(SquirrelTracker.objects.all()),100)
    sightings = []
    for sighting in sightingList:
        sightings.append({'latitude':sighting.Y, 'longitude': sighting.X})
    context = {'sightings':sightings,}
    
    return render(request, 'finder/map.html', context)

def all_sighting(request):
    squirrels= SquirrelTracker.objects.order_by('Unique_Squirrel_ID')
    context= {'squirrel':squirrels
            }
    return render(request, 'finder/all.html', context)

def add_sighting(request):
    if request.method =='POST':
        #check data with form
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SquirrelFinder/sightings/')
    else:
        #build empty form
        form = SquirrelForm()
    context = {
            'form':form,
            }
    return render(request,'finder/edit.html',context)

def edit_sighting(request, Unique_Squirrel_ID):
    squirrel= SquirrelTracker.objects.get( pk = Unique_Squirrel_ID)
    if request.method =='POST':
        #check data with form
        form = SquirrelForm(request.POST, instance= squirrel)
        if form.is_valid():
            form.save()
            return redirect('SquirrelFinder/sightings/')
    else:
        #build empty form
        form = SquirrelForm(instance = squirrel)
    context = {
            'form':form,
            }
    return render(request,'finder/edit.html',context)
