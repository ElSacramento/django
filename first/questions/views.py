from django.shortcuts import render

from django.http import HttpResponse

from models import Restaurant, Dish

def index(request):
	r = Restaurant.objects.all()
	#return HttpResponse("Hello, world. You're at the poll index.")
	return render(request, 'main_template.html', {'restaurants': r})
# Create your views here.

def restaurant(request, urlname):
	r = Restaurant.objects.get(urlname=urlname)
	return render(request, 'main_template.html', {'restaurant': r})	
