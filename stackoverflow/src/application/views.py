from django.shortcuts import render

from django.http import HttpResponse


# def index(request):
# 	r = Restaurant.objects.all()
# 	#return HttpResponse("Hello, world. You're at the poll index.")
# 	return render(request, 'main_template.html', {'restaurants': r})
# # Create your views here.

# def restaurant(request, urlname):
# 	r = Restaurant.objects.get(urlname=urlname)
# 	return render(request, 'main_template.html', {'restaurant': r})	

# def question_text(request):
#     try:
#         id = request.GET.get('id')
#         obj = Question.objects.get(pk=id)
#     except Question.DoesNotExist:
#         raise Http404
#     return HttpResponse(Question.text, content_type='text/plain')
