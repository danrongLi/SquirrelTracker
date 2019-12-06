from django.forms import ModelForm
  
from .models import SquirrelTracker
class SquirrelForm(ModelForm):
    class Meta:
        model = SquirrelTracker
        fields= ['X',
                'Y',
                'Unique_Squirrel_ID',
                'Shift',
                'Date',
                'Age',
                'Primary_Fur_Color',
                'Location',
                'Specific_Location',
                'Running',
                'Chasing',
                'Climbing',
                'Eating',
                'Foraging',
                'Other_Activities',
                'Kuks',
                'Quaas',
                'Tail_Flags',
                'Tail_Twitches',
                'Approaches',
                'Indifferent',
                'Runs_From',
        ]

