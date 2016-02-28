from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse

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
	returnArray = []

	req1 = urllib.request.Request('http://localhost:8001/id/1/')
	req2 = urllib.request.Request('http://localhost:8001/id/2/')
	req3 = urllib.request.Request('http://localhost:8001/id/3/')
	req4 = urllib.request.Request('http://localhost:8001/id/4/')
	req5 = urllib.request.Request('http://localhost:8001/id/5/')
	req6 = urllib.request.Request('http://localhost:8001/id/6/')
	returnArray.append(req1)
	returnArray.append(req2)
	returnArray.append(req3)
	returnArray.append(req4)
	returnArray.append(req5)
	returnArray.append(req6)
	return HttpResponse(json.dumps(returnArray), content_type="application/json") 

def detail(request, sock_id):
	#request from model the details for page
	req = urllib.request.Request('http://localhost:8001/id/' + sock_id + '/')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	return HttpResponse(json.dumps(resp_json, content_type="application/json")
