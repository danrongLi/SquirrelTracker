from django.core.management.base import BaseCommand, CommandError
from SquirrelFinder.models import SquirrelTracker
import csv
import os
class Command(BaseCommand):
   # args = 'vfnx-vebw.csv'
    help = 'Import the csv'
    def add_arguments(self,parser):
        parser.add_argument('path', nargs='+',type = str)
        
    def handle(self, *args, **options):
        for path in options['path']:
            self.stdout.write(self.style.SUCCESS('Reading:{}'.format(path)))
            try:
                with open(path) as csv_file:
                    csv_reader = csv.reader(csv_file,delimiter = ',')
                    for row in csv_reader:
                        if row != "":
                            ST = SquirrelTracker()
                            ST.X = row[0]
                            ST.Y = row[1]
                            ST.Unique_Squirrel_ID = row[2]
                            ST.Hectare = row[3]
                            ST.Shift = row[4]
                            ST.Date = row[5]
                            ST.Hectare_Squirrel_Number = row[6]
                            ST.Age = row[7]
                            ST.Primary_Fur_Color = row[8]
                            ST.Highlight_Fur_Color = row[9]
                            ST.Combination_of_Primary_and_Highlight_Color = row[10]
                            ST.Color_Notes = row[11]
                            ST.Location = row[12]
                            ST.Above_Ground_Sighter_Measurement = row[13]
                            ST.Specific_Location = row[14]
                            ST.Running = row[15]
                            ST.Chasing = row[16]
                            ST.Climbing = row[17]
                            ST.Eating = row[18]
                            ST.Foraging = row[19]
                            ST.Other_Activities = row[20]
                            ST.Kuks = row[21]
                            ST.Quaas = row[22]
                            ST.Moans = row[23]
                            ST.Tail_Flags = row[24]
                            ST.Tail_twitches = row[25]
                            ST.Approaches = row[26]
                            ST.Indifferent = row[27]
                            ST.Runs_From =row[28]
                            ST.Other_Interactions = row[29]
                            ST.Latlong =row[30]
                            ST.save
            except FileNotFoundError:
                raise CommandError("File {} does not exist".format(path))
        
