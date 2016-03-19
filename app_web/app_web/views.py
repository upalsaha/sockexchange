from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse
from . import settings

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
