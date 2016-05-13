from django.shortcuts import redirect
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from django.views.generic import View
from django.views.generic.list import ListView

from .models import *




def index(request):
	context = {}
	template = "index.html"
	return render (request,template,context)

class Dashboard(LoginRequiredMixin, View):
	login_url = '/'

	def get(self, request):
		context = {}
		template = "content/dashboard.html"
		Customers = Customer.objects.all()
		for customer in Customers:
			print customer.id,"---->>"
			for site in customer.sites.all():
				print "Site ->",site.name			
		return render (request, template, context)


class CustomerList(LoginRequiredMixin, ListView):
	login_url ='/'
	template_name = "content/data_customer.html"
	model = Customer

	def get_context_data(self, **kwargs):
		context = super(CustomerList, self).get_context_data(**kwargs)

		return context



# class CustomerDetail(LoginRequiredMixin, DetailView):


def data_conveyor(request):
	if not request.user.is_authenticated():
		return redirect('%s' % ("/"))
	context = {}
	template = "content/data_conveyor.html"
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