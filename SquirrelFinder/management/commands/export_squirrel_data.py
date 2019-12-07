from django.core.management.base import BaseCommand, CommandError
from SquirrelFinder.models import SquirrelTracker
import csv
import os

class Command(BaseCommand):
    help = 'Export the csv'
    def add_arguments(self,parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        with open(options['path'],'w',) as csv_writer:
            parameters = [
                    'x',
                    'y',
                    'unique_squirrel_id',
                    'hectare',
                    'shift',
                    'date',
                    'hectare_squirrel_number',
                    'age',
                    'primary_fur_color',
                    'highlight_fur_color',
                    'combination_of_primary_and',
                    'color_notes',
                    'location',
                    'above_ground_sighter',
                    'specific_location',
                    'running',
                    'chasing',
                    'climbing',
                    'eating',
                    'foraging',
                    'other_activities',
                    'kuks',
                    'quaas',
                    'moans',
                    'tail_flags',
                    'tail_twitches',
                    'approaches',
                    'indifferent',
                    'runs_from',
                    'other_interactions'
                    ]
            writer = csv.DictWriter(csv_writer,fieldnames=parameters)
            writer.writeheader()

            for squirrel in SquirrelTracker.objects.all():
                writer.writerow({
                    'x':squirrel.X,
                    'y':squirrel.Y,
                    'unique_squirrel_id': squirrel.Unique_Squirrel_ID,
                    'hectare': squirrel.Hectare,
                    'shift': squirrel.Shift,
                    'date': squirrel.Date,
                    'hectare_squirrel_number':squirrel.Hectare_Squirrel_Number,
                    'age': squirrel.Age,
                    'primary_fur_color': squirrel.Primary_Fur_Color,
                    'highlight_fur_color': squirrel.Highlight_Fur_Color,
                    'combination_of_primary_and': squirrel.Combination_of_Primary_and_Highlight_Color,
                    'color_notes':squirrel.Color_Notes,
                    'location':squirrel.Location,
                    'above_ground_sighter':squirrel.Above_Ground_Sighter_Measurement,
                    'specific_location': squirrel.Specific_Location,
                    'running': squirrel.Running,
                    'chasing': squirrel.Chasing,
                    'climbing': squirrel.Climbing,
                    'eating': squirrel.Eating,
                    'foraging': squirrel.Foraging,
                    'other_activities': squirrel.Other_Activities,
                    'kuks': squirrel.Kuks,
                    'quaas': squirrel.Quaas,
                    'moans': squirrel.Moans,
                    'tail_flags': squirrel.Tail_Flags,
                    'tail_twitches':squirrel.Tail_Twitches,
                    'approaches': squirrel.Approaches,
                    'indifferent': squirrel.Indifferent,
                    'runs_from': squirrel.Runs_From,
                    'other_interactions': squirrel.Other_Interactions,
                    })
            self.stdout.write(self.style.SUCCESS('Successfully Create:{}'.format(options['path'])))


