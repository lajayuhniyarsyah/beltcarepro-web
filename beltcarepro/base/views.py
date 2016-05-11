from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, Welcome in Beltcarepro 4.0")
