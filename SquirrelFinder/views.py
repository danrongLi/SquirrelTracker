from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import SquirrelTracker
from .forms import SquirrelForm
from django.db.models import Sum, Count
import random
from django.forms import ModelForm
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
    context= {'squirrels':squirrels,
            }
    return render(request, 'finder/all.html', context)

def sighting_stats(request):
    mydict = [
            SquirrelTracker.objects.aggregate(total_squirrels_number = Count('Unique_Squirrel_ID')),
            SquirrelTracker.objects.filter(Age ='Adult').aggregate(num_Adult_number = Count('Unique_Squirrel_ID')),
            SquirrelTracker.objects.filter(Age ='Juvenile').aggregate(num_Juvenile_Squirrels = Count('Unique_Squirrel_ID')),
            SquirrelTracker.objects.filter(Shift ='AM').aggregate(shift_AM_Squirrels_number = Count('Unique_Squirrel_ID')),
            SquirrelTracker.objects.filter(Shift ='PM').aggregate(shift_PM_Squirrels_number = Count('Unique_Squirrel_ID')),
            ]
    sighting_list=[]
    for sighting in mydict:
        sighting_list.append([list(sighting.keys())[0],list(sighting.values())[0]])

    context = {'stats':sighting_list,}
    return render(request, 'finder/sighting_stats.html', context)

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

class SquirrelForm(ModelForm):
    class Meta:
        model=SquirrelTracker
        fields=[
                "X",
                "Y",
                "Unique_Squirrel_ID",
                "Shift",
                "Date",
                "Age",
                "Primary_Fur_Color",
                "Location",
                "Specific_Location",
                "Running",
                "Chasing",
                "Climbing",
                "Eating",
                "Foraging",
                "Other_Activities",
                "Kuks",
                "Quaas",
                "Tail_Flags",
                "Tail_Twitches",
                "Approaches",
                "Indifferent",
                "Runs_From",
                "Other_Interactions",
                "Hectare",
                "Hectare_Squirrel_Number",
                "Latlong",
                "Highlight_Fur_Color",
                "Color_Note",
                "Combination_of_Primary_and_Highlight_Color",
                "Above_Ground_Sighter_Measurement",
                "Moans",
                ]

def edit_sighting(request, Unique_Squirrel_ID):
    #squirrel = get_object_or_404(SquirrelTracker, pk=SquirrelTracker.Unique_Squirrel_ID)
    squirrel= SquirrelTracker.objects.filter( Unique_Squirrel_ID =Unique_Squirrel_ID).first()
    form = SquirrelForm(request.POST or None, instance=squirrel)
    if request.method =='POST':
        #check data with form
        form = SquirrelForm(request.POST, instance= squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/SquirrelFinder/map/')
   # else:
   #     #build empty form
   #     form = SquirrelForm(instance = squirrel)
    context = {
            'form':form,
            'squirrel':squirrel,
            }
    return render(request,'finder/edit.html',context)
