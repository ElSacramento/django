from django.core.management.base import BaseCommand, CommandError
from question.models import Question, Answer
from user_page.models import User
import argparse

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('-user_id', type=int)
        parser.add_argument('-question_id', type=int)
        parser.add_argument('--text', nargs='+')
        
    def handle(self, *args, **options):
        user_id = options['user_id']
        question_id = options['question_id']
        text = ""
        for text_i in options['text']:
        	text += str(text_i) +  " " 
        name = Answer(user_id=user_id, question_id=question_id, text=text)
        name.save()
        
        # self.stdout.write("Done", ending='')
