from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Sock
from .models import User
import json 

# Create your views here.
from django.http import HttpResponse

def home(request):
    home_socks = Sock.objects.order_by('?')
    dict = {}

    for x in range(1, 7):
    	current = home_socks[x].as_json()
    	dict['name' + str(x)] = current['name']
    	dict['color' + str(x)] = current['color']
    	dict['id' + str(x)] = current['id']

    return HttpResponse(json.dumps(dict), content_type="application/json")

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

def sign_up(request):
	if request.method == 'GET':
		return render('home')
	if request.method == 'POST':
		new_user = User.objects.create(username=request.POST.get("username"), password=request.POST.get("password"))
		new_user.save()
	return HttpResponse("OK")