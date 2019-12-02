from django.core.management.base import BaseCommand, CommandError
from .models import Profile
import csv

class Command(BaseCommand):
    help = 'Lets open the csv'

    def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        self.stdout.write(args[0])

        with open(args[0], 'rb') as file:
            rows = csv.reader(file, delimiter=",", quotechar='"')



        for poll_id in options['poll_ids']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
