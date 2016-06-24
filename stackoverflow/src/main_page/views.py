from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from question.models import Question, Tag
from django.core.paginator import Paginator

class QuestionsListBest(ListView):
    template_name = 'list_question.html'
    model = Question
    queryset = Question.objects.best_posts() 
    paginate_by = 5    

class QuestionsListNew(ListView):
    template_name = 'list_question.html'
    model = Question
    queryset = Question.objects.new_posts()
    paginate_by = 5

# class QuestionsListTag(ListView):
#     template_name = 'list_question.html'
#     model = Question
#     paginate_by = 5
#     def get_queryset(self):
#         tag=self.kwargs['tag']
#         return Question.objects.filter(tags__title__in=[tag])

class QuestionsListTag(ListView):
    template_name = 'list_question.html'
    paginate_by = 5
    def get_queryset(self):
        return Question.objects.posts_by_tag(self.kwargs['tag'])
