from django.http import HttpResponse
from .models import Pet
from django.shortcuts import render
# Create your views here.
import random

def all_squirrels(request):
    squirrels = SquirrelTracker.objects.all()
    context = {
            'squirrels':squirrels,
            }
    return render(request, 'sightings/all.html',context)
