from django.db import models
from django.utils.translation import gettext as _
class SquirrelTracker(models.Model):
    X = models.FloatField (  
        help_text = ('Latitude'),
        max_length = 50,
        )
    Y = models.FloatField(
        help_text = ('Longitude'),
        max_length = 50,
        )
    Unique_Squirrel_ID=models.CharField(
        help_text = ('Unique Squirrel Id'),
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
    Date = models.DateField(
        help_text = ('date'),
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
    Running = models.BooleanField(
        help_text = ('Running?'),
        default = False,)
    Chasing = models.BooleanField(
        help_text = ('Chasing?'),
        default = False,)
    Climbing = models.BooleanField(
        help_text = ('Climbing?'),
        default = False,)
    Eating = models.BooleanField(
        help_text = ('Eating?'),
        default = False,)
    Foraging = models.BooleanField(
        help_text = ('Foraging?'),
        default = False,)
    Other_Activities = models.CharField(
        help_text = ('Other Activities'),
        max_length = 50,
        null = True,
        )
    Kuks = models.BooleanField(
        help_text = ('Kuks?'),
        default = False,)
    Quaas = models.BooleanField(
        help_text = ('Quaas?'),
        default = False,)
    Tail_Flags = models.BooleanField(
        help_text = ('Tail Flags?'),
        default = False,)
    Tail_Twitches = models.BooleanField(
        help_text = ('Tail Twitches?'),
        default = False,)
    Approaches = models.BooleanField(
        help_text = ('Approaches?'),
        default = False,)
    Indifferent = models.BooleanField(
        help_text = ('Indifferent?'),
        default = False,)
    Runs_From = models.BooleanField(
        help_text = ('Runs From?'),
        default = False,)
    Other_Interactions = models.CharField(
        help_text = ('Others Interactions'),
        max_length = 50,
        null = True,)
    Hectare = models.CharField(
        help_text = ('Hectare'),
        max_length = 50,)
    Hectare_Squirrel_Number = models.IntegerField(
        help_text = ('Squirrel Number'),)
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
    Moans = models.BooleanField(
            help_text='Moans',
            default = False,)
    

    def __str__(self):
        return self.name

