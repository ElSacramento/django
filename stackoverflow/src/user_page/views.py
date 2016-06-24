from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

def user_page(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('../log_in/')
	else:
		return render(request, 'profile.html')