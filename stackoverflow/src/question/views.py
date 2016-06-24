from django.shortcuts import render
from django.http import Http404
from .models import Question
from .forms import QuestionForm, AnswerForm
from django.http import HttpResponse, HttpResponseRedirect

def question(request):
	return render(request, 'json.html')

def get_question(request, question_id):
	try:
	    question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
    		raise Http404("Question does not exist")
 	return render(request, 'question.html', {'question': question})

def add_question(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('../../log_in/')
    else:
        if request.method == 'POST':
            u = Question(user=request.user)
            form = QuestionForm(data=request.POST, instance=u)
            if form.is_valid():
                question = form.save()
                full_url = '../' + str(question.pk) + '/'
                return HttpResponseRedirect(full_url)
            else:
        	   return render(request, "add_question.html", {'form':form })
        else:
    	   return render(request, "add_question.html", {'form':QuestionForm() })

def question_answer(request):
    if request.method == 'GET':
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            raise Http404("Question does not exist")
        return render(request, 'question.html', {'question': question})
    else:
        if request.method == 'POST':
            if not request.user.is_authenticated():
                return HttpResponseRedirect('../../log_in/')
            u = Answer(user=request.user)
            question = request.question
            form = AnswerForm(data=request.POST, instance=u)
            if form.is_valid():
                answer = form.save()
                question.set_answers(answer)
                full_url = '../' + str(question.pk) + '/'
                return HttpResponseRedirect(full_url)
            else:
               return render(request, "question.html", {'form':form })
        else:
           return render(request, "question.html", {'form':AnswerForm() })