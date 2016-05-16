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
	if request.user.is_authenticated():
		return redirect('%s' % ("/dashboard/"))
	context = {}
	template = "index.html"
	return render (request,template,context)

class Dashboard(LoginRequiredMixin, View):
	login_url = '/'

	def get(self, request):
		context = {}
		template = "content/dashboard.html"
		return render (request, template, context)


class CustomerList(LoginRequiredMixin, ListView):
	login_url ='/'
	template_name = "content/data_customer.html"
	model = Customer

	def get_context_data(self, **kwargs):
		context = super(CustomerList, self).get_context_data(**kwargs)

		return context


class SiteList(LoginRequiredMixin, ListView):
	login_url ='/'
	template_name = "content/data_site.html"
	model = Site

	def get_context_data(self, **kwargs):
		context = super(SiteList, self).get_context_data(**kwargs)

		return context


class AreaList(LoginRequiredMixin, ListView):
	login_url ='/'
	template_name = "content/data_area.html"
	model = Area

	def get_context_data(self, **kwargs):
		context = super(AreaList, self).get_context_data(**kwargs)

		return context


class ConveyorList(LoginRequiredMixin, ListView):
	login_url ='/'
	template_name = "content/data_conveyor.html"
	model = Conveyor

	def get_context_data(self, **kwargs):
		context = super(ConveyorList, self).get_context_data(**kwargs)

		return context


class ConveyorAssetList(LoginRequiredMixin, ListView):
	login_url ='/'
	template_name = "content/data_conveyor_asset.html"
	model = ConveyorAsset

	def get_context_data(self, **kwargs):
		context = super(ConveyorAssetList, self).get_context_data(**kwargs)

		return context
		

# class CustomerDetail(LoginRequiredMixin, DetailView):

def view_conveyor(request):
	context = {"range":range(100)}
	template = "content/view_conveyor.html"
	return render (request,template,context)

def add_conveyor(request):
	context = {"range":range(8)}
	template = "content/add_conveyor.html"
	return render (request,template,context)

def view_customer(request):
	context = {"range":range(10)}
	template = "content/view_customer.html"
	return render (request,template,context)

def add_customer(request):
	context = {}
	template = "content/add_customer.html"
	return render (request,template,context)

def view_site(request):
	context = {"range":range(10)}
	template = "content/view_site.html"
	return render (request,template,context)

def add_customer_site(request):
	context = {}
	template = "content/add_customer_site.html"
	return render (request,template,context)

def view_area(request):
	context = {"range":range(5)}
	template = "content/view_area.html"
	return render (request,template,context)

def add_area(request):
	context = {"range":range(4)}
	template = "content/add_area.html"
	return render (request,template,context)

def detail_conveyor_condition(request):
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
		
		return HttpResponse(json.dumps(response_data), content_type="application/json")  