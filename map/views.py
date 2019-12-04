# the view file after map

from django.http import HttpResponse
from django.shortcuts import render
from .models import SquirrelTracker

# Create your views here.

def index(request):
    return HttpResponse('Hi! How are you !!!')

def map(request):
    squirrels = SquirrelTracker.objects.all()
    context = {
            'Squirrel':squirrels,
            }
    return render(request, 'map.html', context)
