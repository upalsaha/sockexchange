from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import settings
from .forms import SignUpForm

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
			#result = urllib2.Request(url, urllib.urlencode(post_data))
			enc_data = urllib.parse.urlencode(post_data)
			bin_data = enc_data.encode('ascii')
			req = urllib.request.Request(url)
			result = urllib.request.urlopen(req, bin_data)

			return HttpResponseRedirect('/home/')
	# if a GET (or any other method) we'll create a blank form
	else:
		form = SignUpForm()
		
	return render(request, 'signup.html', {'form': form})

def login(request):
	response = 'invalid'
	if request.method == 'POST':
		# create a form instance and populate it from the request
		form = LoginForm(request.POST)
		# check whether it's valid
		if form.is_valid():
			url = 'http://' + settings.EXP_API + ':8000/login/'

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			post_data = {'username':username, 'password': password}
			#result = urllib2.Request(url, urllib.urlencode(post_data))
			enc_data = urllib.parse.urlencode(post_data)
			bin_data = enc_data.encode('ascii')
			req = urllib.request.Request(url)
			result = urllib.request.urlopen(req, bin_data)

			return HttpResponseRedirect('/home/')
	# if a GET (or any other method) we'll create a blank form
	else:
		form = LoginForm()
		
	return render(request, 'signup.html', {'form': form})