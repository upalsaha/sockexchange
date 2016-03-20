from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse
from . import settings

import json
import requests
import urllib.request
import urllib.parse

def home(request):

	url = 'http://' + settings.MODELS_API + ':8000/home/'
	reqJSON = urllib.request.Request(url)
	resp = urllib.request.urlopen(reqJSON).read().decode('utf-8')

	return HttpResponse(resp, content_type="application/json") 

def detail(request, sock_id):

	url = 'http://' + settings.MODELS_API + ':8000/id/' + str(sock_id) + '/'
	req = urllib.request.Request(url)
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')

	return HttpResponse(resp_json, content_type="application/json")

def sign_up(request):
	response = "invalid"
	if request.method == 'GET':
		return render('home')
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		url = 'http://' + settings.MODELS_API + ':8000/signup/'

		post_data = {'username':username, 'password': password}
		enc_data = urllib.parse.urlencode(post_data)
		bin_data = enc_data.encode('ascii')
		req = urllib.request.Request(url)
		result = urllib.request.urlopen(req, bin_data)

	return HttpResponse(result)