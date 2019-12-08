from django.core.management.base import BaseCommand, CommandError
from SquirrelFinder.models import SquirrelTracker
import csv
import os
import datetime

class Command(BaseCommand):
    help = 'Import the csv'
    def add_arguments(self,parser):
        parser.add_argument('path', nargs='+',type = str)
        
    def handle(self, *args, **options):

        def to_boo(text):
            if text.lower() == 'true':
                return True
            elif text.lower()=='false':
                return False
            else:
                return None


        for path in options['path']:
            self.stdout.write(self.style.SUCCESS('Reading:{}'.format(path)))
            with open(path) as csv_file:
                csv_reader = csv.DictReader(csv_file)
                data = list(csv_reader)
                for row in data:
                    ST = SquirrelTracker()
                    ST.X = float(row['x'])
                    ST.Y = float(row['y'])
                    ST.Unique_Squirrel_ID = row['unique_squirrel_id']
                    ST.Shift = row['shift']
                    ST.Date = datetime.datetime.strptime(row['date'],'%m%d%Y')
                    ST.Age = row['age']
                    ST.Primary_Fur_Color = row['primary_fur_color']
                    ST.Location = row['location']
                    ST.Specific_Location = row['specific_location']
                    ST.Running = to_boo(row['running'])
                    ST.Chasing = to_boo(row['chasing'])
                    ST.Climbing = to_boo(row['climbing'])
                    ST.Eating = to_boo(row['eating'])
                    ST.Foraging = to_boo(row['foraging'])
                    ST.Other_Activities = row['other_activities']
                    ST.Kuks = to_boo(row['kuks'])
                    ST.Quaas = to_boo(row['quaas'])
                    ST.Moans = to_boo(row['moans'])
                    ST.Tail_Flags = to_boo(row['tail_flags'])
                    ST.Tail_Twitches = to_boo(row['tail_twitches'])
                    ST.Approaches = to_boo(row['approaches'])
                    ST.Indifferent = to_boo(row['indifferent'])
                    ST.Runs_From =to_boo(row['runs_from'])
                    ST.save()
