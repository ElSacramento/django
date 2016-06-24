from django.shortcuts import render

from django.http import HttpResponse

def add_question(request):
	return render(request, 'add_question.html')
