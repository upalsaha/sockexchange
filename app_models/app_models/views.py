from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Sock
from .models import User
from .models import Authenticator
from . import settings
from django.contrib.auth import hashers
import json
import hmac
import os

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
		return HttpResponse('BAD')
	hashed_password = hashers.make_password(request.POST['password'])
	if request.method == 'POST':
		new_user = User.objects.create(username=request.POST.get("username"), password=hashed_password)
		new_user.save()
	return HttpResponse("OK")

def login(request):
	if request.method == 'GET':
		try_username = request.GET.get('username')
		try_password = request.GET.get('password')
		try:
			u = User.objects.get(username=try_username)
		except User.DoesNotExist:
			return HttpResponse("BAD: USER DNE")
		if hashers.check_password(try_password, u.password):
			auth = hmac.new (key = settings.SECRET_KEY.encode('utf-8'), msg = os.urandom(32), digestmod = 'sha256').hexdigest()
			logged_in = Authenticator.objects.create(user_id=u, auth=auth)
			logged_in.save()
			return HttpResponse(auth)
		else:
			return HttpResponse("BAD: PASSWORD")
	else:
		return HttpResponse("BAD: POST REQ")