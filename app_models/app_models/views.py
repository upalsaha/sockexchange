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
    home_socks = Sock.objects.order_by('?')[:6]
    #home_socks = Sock.objects.order_by()
    dict = {}
    x = 1
    for sock in home_socks:
    	current = sock.as_dict()
    	dict['name' + str(x)] = current['name']
    	dict['color' + str(x)] = current['color']
    	dict['id' + str(x)] = current['id']
    	x += 1
    #return JSON of 6 random socks
    return HttpResponse(json.dumps(dict), content_type="application/json")

def id(request, sock_id):
	sock = get_object_or_404(Sock, pk=sock_id)
	return HttpResponse(json.dumps(sock.as_dict()), content_type="application/json")

def material(request, material):
	sock = get_list_or_404(Sock, material=material)
	results = [ob.as_dict() for ob in sock]
	return HttpResponse(json.dumps(results), content_type="application/json")

def color(request, color):
	sock = get_list_or_404(Sock, color=color)
	results = [ob.as_dict() for ob in sock]
	return HttpResponse(json.dumps(results), content_type="application/json")

def theme(request, theme):
	sock = get_list_or_404(Sock, theme=theme)
	results = [ob.as_dict() for ob in sock]
	return HttpResponse(json.dumps(results), content_type="application/json")

def sign_up(request):
	if request.method == 'GET':
		dict = {}
		dict['result'] = 1
		dict['message'] = "Error: Get request made to sign_up on models level"
		return HttpResponse(json.dumps(dict), content_type="application/json")
	hashed_password = hashers.make_password(request.POST['password'])
	if request.method == 'POST':
		new_user = User.objects.create(username=request.POST.get("username"), password=hashed_password)
		new_user.save()
	dict = {}
	dict['result'] = 0
	dict['message'] = "New user created"
	return HttpResponse(json.dumps(dict), content_type='application/json')


def login(request):
	if request.method == 'GET':
		try_username = request.GET.get('username')
		try_password = request.GET.get('password')
		try:
			u = User.objects.get(username=try_username)
		except User.DoesNotExist:
			return HttpResponse("BAD")
		if hashers.check_password(try_password, u.password):
			auth = hmac.new(key = settings.SECRET_KEY.encode('utf-8'), msg = os.urandom(32), digestmod = 'sha256').hexdigest()
			logged_in = Authenticator.objects.create(user_id=u, auth=auth)
			logged_in.save()
			dict = {}
			dict['auth'] = auth
			return HttpResponse(json.dumps(dict), content_type="application/json")
		else:
			return HttpResponse("BAD")
	else:
		return HttpResponse("BAD")

def logout(request):
	auth = request.GET.get('auth')
	if request.method == 'GET':
		Authenticator.objects.filter(auth=auth).delete()
		return HttpResponse('OK')
	else:
		return HttpResponse('BAD')

def create(request):
	if request.method == 'GET':
		return HttpResponse('BAD')
	if request.method == 'POST':
		name = request.POST.get('name')
		material = request.POST.get('material')
		color = request.POST.get('color')
		description = request.POST.get('description')
		style = request.POST.get('style')
		theme = request.POST.get('theme')
		price = request.POST.get('price')

		auth_val = request.POST.get('auth')
		linked_auth = Authenticator.objects.get(auth=auth_val)
		seller = linked_auth.user_id

		new_sock = Sock.objects.create(name=name, material=material, color=color, description=description, style=style, theme=theme, price=price, seller=seller)
		new_sock.save()

	return HttpResponse(new_sock.pk)

def verify(request):
	if request.method == 'GET':
		auth = request.GET.get('auth')
		try:
			u = Authenticator.objects.get(auth=auth)
		except Authenticator.DoesNotExist:
			return HttpResponse("BAD")
	return HttpResponse('OK')