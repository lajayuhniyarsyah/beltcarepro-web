from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
import json

def index(request):
	context = {}
	template = "index.html"
	return render (request,template,context)


def dashboard(request):
	if not request.user.is_authenticated():
		return redirect('%s' % ("/"))
	context = {}
	template = "content/dashboard.html"
	return render (request,template,context)

def data_conveyor(request):
	if not request.user.is_authenticated():
		return redirect('%s' % ("/"))
	context = {}
	template = "content/data_conveyor.html"
	return render (request,template,context)

def data_customer(request):
	if not request.user.is_authenticated():
		return redirect('%s' % ("/"))
	context = {}
	context = {"range":range(100)}
	template = "content/data_customer.html"
	return render (request,template,context)

def data_site(request):
	if not request.user.is_authenticated():
		return redirect('%s' % ("/"))
	context = {}
	template = "content/data_site.html"
	return render (request,template,context)

def detail_conveyor_condition(request):
	if not request.user.is_authenticated():
		return redirect('%s' % ("/"))
	context = {"part":["Belt Conveyor","SECTION SPLICE BELT","Pulley","ROLLER","PRIMARY Cleaners","Secondary Cleaners"]}
	template = "content/detail_conveyor_condition.html"
	return render (request,template,context)

def login_custom(request):

	if request.method == 'POST':   
		username = request.POST['username']
  		password = request.POST['passwd']                                                                                                                                                                                                        
		login_form =  authenticate(username=username, password=password)
		response_data = {}                                                                              
		if login_form is not None:
			if login_form.is_active:
				login(request,login_form)
				response_data['accessGranted'] = 'Success!'
				response_data['result'] = 'Success!'
				response_data['message'] = 'You"re logged in' 		
		else:
			response_data['result'] = 'failed'
			response_data['message'] = 'You messed up'   
		print response_data['result'],"<<<<<<<<<<<<<<<"
		return HttpResponse(json.dumps(response_data), content_type="application/json")  