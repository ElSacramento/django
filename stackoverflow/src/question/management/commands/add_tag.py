from django.core.management.base import BaseCommand, CommandError
from question.models import Tag

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('arg', nargs='+')
        
    def handle(self, *args, **options):
    	for tag in options['arg']:
        	name = Tag(title=tag)
        	name.save()
        
        # self.stdout.write("Done", ending='')
