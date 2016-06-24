from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm

# def log_in(request):
# 	return render(request, 'login.html')


from django.contrib import messages 

            
def log_in(request):
    args = {}
    form = LoginForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            user = form.login(request)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('../main_page/')
            else:
                render(request, "login.html", {'form':form })
        else:
            return render(request, "login.html", {'form':form })
    return render(request, "login.html", {'login_form': LoginForm() })

def log_out(request):
    auth.logout(request)
    return HttpResponseRedirect('../../main_page/')