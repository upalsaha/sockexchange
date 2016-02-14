from django.shortcuts import get_object_or_404, render
from .models import Sock
import json 

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def id(request, sock_id):
	sock = get_object_or_404(Sock, pk=sock_id)
	return HttpResponse(json.dumps(sock.as_json()), content_type="application/json")

	#response = "You're looking at the results of sock %s."


def material(request, material):
	response = "You're looking at the results of sock %s."
	return HttpResponse(response % material)

def color(request, color):
	response = "You're looking at the results of sock %s."
	return HttpResponse(response % color)	

def theme(request, theme):
	response = "You're looking at the results of sock %s."
	return HttpResponse(response % theme)	


	#return HttpResponse(json.dumps(result.as_json()), content_type="application/json")
