from django.forms import ModelForm
  
from .models import SquirrelTracker
class SquirrelForm(ModelForm):
    class Meta:
        model = SquirrelTracker
        fields= '__all__'

