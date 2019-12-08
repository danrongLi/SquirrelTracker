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
        unique = True,
        primary_key=True,
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
    Moans = models.BooleanField(
            help_text='Moans',
            default = False,)
    
    def __str__(self):
        return self.Unique_Squirrel_ID


