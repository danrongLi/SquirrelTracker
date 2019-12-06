from django.db import models
from django.utils.translation import gettext as _

class SquirrelTracker(models.Model):
    X = models.FloatField (  
        help_text = ('Longitude'),
        )
    Y = models.FloatField(
        help_text = ('Latitude'),
        )
    Unique_Squirrel_ID=models.CharField(
        help_text = ('Unique Squirrel ID'),
        max_length = 50,
        )
    PM = 'PM'
    AM = 'AM'

    SHIFT_CHOICES = (
        (PM,'PM'),
        (AM,'AM'),
        )
    Shift = models.CharField(
        help_text = ('shift'),
        max_length = 50,
        choices = SHIFT_CHOICES,
        )
    Date = models.CharField(
        help_text = ('date'),
        max_length = 50,
        )
    ADULT='Adult'
    JUVENILE='Juvenile'

    AGE_CHOICES = (
        (ADULT,'Adult'),
        (JUVENILE,'Juvenile'),
        )

    Age = models.CharField(
        help_text = ('Age'),
        max_length = 50,
        choices = AGE_CHOICES,
        null = True,
        )
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'

    FUR_COLOR_CHOICES = (
        (GRAY,'Gray'),
        (CINNAMON,'Cinnamon'),
        (BLACK,'Black'),
        )

    Primary_Fur_Color = models.CharField(
        help_text = ('Primary Fur Color'),
        max_length = 50,
        choices = FUR_COLOR_CHOICES,
        null = True,
        )
    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'

    LOCATION_CHOICES = (
        (GROUND_PLANE,'Ground Plane'),
        (ABOVE_GROUND,'Above Ground'),
        )
    Location = models.CharField(
        help_text = ('Location'),
        max_length = 50,
        choices = LOCATION_CHOICES,
        null = True,
        )
    Specific_Location = models.CharField(
        help_text = ('Specific Location'),
        max_length = 50,
        null = True,
        )
    Running = models.CharField(
        help_text = ('Running?'),
        max_length = 50,)
    Chasing = models.CharField(
        help_text = ('Chasing?'),
        max_length = 50,)
    Climbing = models.CharField(
        help_text = ('Climbing?'),
        max_length =50,)
    Eating = models.CharField(
        help_text = ('Eating?'),
        max_length = 50,)
    Foraging = models.CharField(
        help_text = ('Foraging?'),
        max_length = 50,)
    Other_Activities = models.CharField(
        help_text = ('Other Activities'),
        max_length = 50,
        null = True,
        )
    Kuks = models.CharField(
        help_text = ('Kuks?'),
        max_length=50,)
    Quaas = models.CharField(
        help_text = ('Quaas?'),
        max_length = 50,)
    Tail_Flags = models.CharField(
        help_text = ('Tail Flags?'),
        max_length =50,)
    Tail_Twitches = models.CharField(
        help_text = ('Tail Twitches?'),
        max_length = 50,)
    Approaches = models.CharField(
        help_text = ('Approaches?'),
        max_length = 50,)
    Indifferent = models.CharField(
        help_text = ('Indifferent?'),
        max_length = 50,)
    Runs_From = models.CharField(
        help_text = ('Runs From?'),
        max_length = 50,)
    Other_Interactions = models.CharField(
        help_text = ('Others Interactions'),
        max_length = 50,
        null = True,)
    Hectare = models.CharField(
        help_text = ('Hectare'),
        max_length = 50,)
    Hectare_Squirrel_Number = models.CharField(
        help_text = ('Squirrel Number'),
        max_length = 50,)
    Latlong = models.CharField(
        help_text = ('LatLong Point'),
        max_length = 50,
        )
    Highlight_Fur_Color = models.CharField(
        help_text = ('Highlight Fur Color'),
        max_length = 50,
        )
    Color_Note = models.CharField(
        help_text = ('Color Note'),
        max_length = 50,)
    Combination_of_Primary_and_Highlight_Color = models.CharField(
        help_text = ('Combination of Primary and Highlight'),
        max_length = 50,)
    Above_Ground_Sighter_Measurement = models.CharField(
            help_text = ('Above Ground Sighter Measurement'),
            max_length = 50,
            null = True,
            )
    Moans = models.CharField(
            help_text='Moans',
            max_length = 50,)
    
    def __str__(self):
        return self.Unique_Squirrel_ID
    #def __str__(self):
       # return self.name

