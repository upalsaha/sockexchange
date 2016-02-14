from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Sock
import json 

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def id(request, sock_id):
	sock = get_object_or_404(Sock, pk=sock_id)
	return HttpResponse(json.dumps(sock.as_json()), content_type="application/json")

def material(request, material):
	sock = get_list_or_404(Sock, material=material)
	results = [ob.as_json() for ob in sock]
	return HttpResponse(json.dumps(results), content_type="application/json")

def color(request, color):
	sock = get_list_or_404(Sock, color=color)
	results = [ob.as_json() for ob in sock]
	return HttpResponse(json.dumps(results), content_type="application/json")

def theme(request, theme):
	sock = get_list_or_404(Sock, theme=theme)
	results = [ob.as_json() for ob in sock]
	return HttpResponse(json.dumps(results), content_type="application/json")

