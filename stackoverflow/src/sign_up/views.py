from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from .forms import RegistrationForm
from user_page.models import User

def register(request):
    """
    User registration view.
    """
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
        	user = form.save()
		return HttpResponseRedirect('../user_page/')
        else:
        	return render(request, "signup.html", {'form':form })
    else:
    	return render(request, "signup.html", {'form':RegistrationForm() })