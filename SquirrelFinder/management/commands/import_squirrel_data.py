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
        csvPath = args[0]
        if not os.path.exists (csvPath):
            raise CommandError ("%s doesnt exist." %csvPath)
        model, _ = os.path.splitext (os.path.basename(csvPath))
        Model = get_model ("SquirrelTracker", model.title ())
        if not Model:
            raise CommandError ("%s Model doesn't exist'")
        model_fields = [f.name for f in Model._meta.fields]
        fields_name = []
        with open (csvPath, 'rb') as csvFile:
            reader = csv.reader (csvFile, delimiter=',', quotechar="\"")
            fields_name = reader.next ()
            for i, _ in enumerate(fields_name):
                fields_name[i] = fields_name[i].lower ()
                fields_name[i] = fields_name[i].replace (' ', '_')
                if not fields_name[i] in model_fields:
                    raise CommandError ("%s field doesn't exists in %s Model" %(fields_name[i], Model))
            for row in reader:
                try:
                    obj = Model()
                    for i, field in enumerate(row):
                        setattr (obj, fields_name[i], field)
                    obj.save ()
                except Exception as e:
                    raise CommandError(e)        

