from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from . import settings
from .forms import SignUpForm
from .forms import LoginForm
from .forms import CreateForm
from django.contrib import messages

import json 
import urllib.request
import urllib.parse

def home(request):
	# make a GET request and parse the returned JSON
	url = 'http://' + settings.EXP_API + ':8000/home/'
	req = urllib.request.Request(url)

	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	return render(request, 'index.html', resp)

def detail(request, sock_id):
	#request from model the details for page
	req = urllib.request.Request('http://' + settings.EXP_API + ':8000/detail/' + sock_id + '/')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	return render(request, 'detail.html', resp)

def sign_up(request):
	response = 'invalid'
	if request.method == 'POST':
		# create a form instance and populate it from the request
		form = SignUpForm(request.POST)
		# check whether it's valid
		if form.is_valid():
			url = 'http://' + settings.EXP_API + ':8000/signup/'

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			post_data = {'username':username, 'password': password}
			enc_data = urllib.parse.urlencode(post_data)
			bin_data = enc_data.encode('ascii')
			req = urllib.request.Request(url)
			result = urllib.request.urlopen(req, bin_data).read().decode('utf-8')
			result_dict = json.loads(result);
			messages.success(request, result_dict['message'])

			return HttpResponseRedirect('/home/')
	# if a GET (or any other method) we'll create a blank form
	else:
		form = SignUpForm()
		
	return render(request, 'signup.html', {'form': form})

def login(request):

	response = 'invalid'
	if request.COOKIES.get('auth'):
		messages.error(request, "Already logged in")
		return HttpResponseRedirect('/home/')
	if request.method == 'GET':
		next_url = request.GET.get('next') or reverse('home')
		dict = {}
		dict['next'] = next_url
		form = LoginForm()

		dict['form'] = form;
		return render(request, 'login.html', dict)

	if request.method == 'POST':
		# create a form instance and populate it from the request
		form = LoginForm(request.POST)
		# check whether it's valid
		if form.is_valid():
			url = 'http://' + settings.EXP_API + ':8000/login/'
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			next_url = form.cleaned_data.get('next') or reverse('home')
			post_data = {'username':username, 'password': password}
			enc_data = urllib.parse.urlencode(post_data)
			bin_data = enc_data.encode('ascii')
			req = urllib.request.Request(url)
			result = urllib.request.urlopen(req, bin_data).read().decode('utf-8')
			if not result:
				dict = {}
				dict['next'] = next_url
				return render(request, 'login.html', dict)
			if result == 'BAD':
				dict = {}
				dict['next'] = next_url
				return render(request, 'login.html', dict)

			authenticator = json.loads(result)
			if authenticator['auth'] == "BAD":
				dict = {}
				dict['next'] = next_url
				return render(request, 'login.html', dict)
			else:
				response = HttpResponseRedirect(next_url)
				response.set_cookie("auth", authenticator['auth'])
				return response

	# if a GET (or any other method) we'll create a blank form
	else:
		form = LoginForm()
		
	return render(request, 'login.html', {'form': form})

def logout(request):
	auth = request.COOKIES.get('auth')
	if not auth:
		messages.error(request, "Not logged in")
		return HttpResponseRedirect('/home/')
	url = 'http://' + settings.EXP_API + ':8000/logout/'
	post_data = {'auth': auth}
	enc_data = urllib.parse.urlencode(post_data)
	bin_data = enc_data.encode('ascii')
	req = urllib.request.Request(url)
	result = urllib.request.urlopen(req, bin_data).read().decode('utf-8')
	if result == 'OK':
		messages.success(request, "Successfully logged out")
	else:
		messages.error(request, "ERROR: Unable to log out")
	response = HttpResponseRedirect('/home/')
	response.delete_cookie('auth')
	return response

def create(request):
	auth = request.COOKIES.get('auth')
	if not auth:
		messages.error(request, "Not logged in")
		return HttpResponseRedirect('/home/')
	if request.method == 'POST':
		# create a form instance and populate it from the request
		form = CreateForm(request.POST)
		# check whether it's valid
		if form.is_valid():
			url = 'http://' + settings.EXP_API + ':8000/create/'

			name = form.cleaned_data['name']
			material = form.cleaned_data['material']
			color = form.cleaned_data['color']
			description = form.cleaned_data['description']
			style = form.cleaned_data['style']
			theme = form.cleaned_data['theme']
			price = form.cleaned_data['price']

			post_data = {'name': name, 'material': material, 'color': color, 'description': description, 'style': style, 'theme': theme, 'price': price, 'auth': auth}
			enc_data = urllib.parse.urlencode(post_data)
			bin_data = enc_data.encode('ascii')
			req = urllib.request.Request(url)
			result = urllib.request.urlopen(req, bin_data)
			messages.success(request, "Listing created successfully")

			return HttpResponseRedirect('/home/')
	# if a GET (or any other method) we'll create a blank form
	else:
		form = CreateForm()
		
	return render(request, 'createlisting.html', {'form': form})

def search(request):
	if request.method == 'POST':
		query = request.POST.get('query')
		url = 'http://' + settings.EXP_API + ':8000/search?query=' + query
		req = urllib.request.Request(url)
		response = urllib.request.urlopen(req).read().decode('utf-8')
		search_results = json.loads(response)

		return render(request, 'searchresults.html', { 'dict': search_results})

