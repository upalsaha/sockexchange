from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse
from . import settings

import json 
import urllib.request
import urllib.parse

# make a GET request and parse the returned JSON                                                                                                                                                           # note, no timeouts, error handling or all the other things needed to do this for real                                                                                                                      
# print ("About to do the GET...")
# req = urllib.request.Request('http://jsonplaceholder.typicode.com/posts/1')
# resp_json = urllib.request.urlopen(req).read().decode('utf-8')
# resp = json.loads(resp_json)
# print(resp)

def home(request):
	# make a GET request and parse the returned JSON                                                                                                                                                           # note, no timeouts, error handling or all the other things needed to do this for real                                                                                                                      
	#req = urllib.request.Request('http://localhost:8002/home/')
	url = 'http://' + settings.EXP_API + ':8000/home/'
	req = urllib.request.Request(url)

	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	return render(request, 'index.html', resp)

def detail(request, sock_id):
	#request from model the details for page
	#req = urllib.request.Request('http://localhost:8002/detail/' + sock_id + '/')
	req = urllib.request.Request('http://' + settings.EXP_API + ':8000/detail/' + sock_id + '/')

	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	return render(request, 'templates/detail.html', resp)
