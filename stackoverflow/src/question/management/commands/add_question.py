from django.core.management.base import BaseCommand, CommandError
from question.models import Question
from user_page.models import User
import argparse

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('-user_id', type=int)
        parser.add_argument('--title', nargs='+')
        parser.add_argument('--text', nargs='+')
        
    def handle(self, *args, **options):
        user_id = options['user_id']
        title = ""
        for text_i in options['title']:
        	title += str(text_i) +  " " 
        text = ""
        for text_i in options['text']:
        	text += str(text_i) +  " " 
        name = Question(title=title, user_id=user_id, text=text)
        name.save()
        
        # self.stdout.write("Done", ending='')
