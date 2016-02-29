from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse
​
import json 
import urllib.request
import urllib.parse
​
def home(request):
​
	dict = {}
​
	req1JSON = urllib.request.Request('http://localhost:8001/id/1/')
	resp1 = urllib.request.urlopen(req1JSON).read().decode('utf-8')
	resp1_json = json.loads(resp1)
	dict['name1'] = resp1_json['name']
	dict['color1'] = resp1_json['color']
	dict['id1'] = resp1_json['id']
​
	req2JSON = urllib.request.Request('http://localhost:8001/id/2/')
	resp2 = urllib.request.urlopen(req2JSON).read().decode('utf-8')
	resp2_json = json.loads(resp2)
​
	dict['name2'] = resp2_json['name']
	dict['color2'] = resp2_json['color']
	dict['id2'] = resp1_json['id']
​
	req3JSON = urllib.request.Request('http://localhost:8001/id/3/')
	resp3 = urllib.request.urlopen(req3JSON).read().decode('utf-8')
	resp3_json = json.loads(resp3)
​
	dict['name3'] = resp3_json['name']
	dict['color3'] = resp3_json['color']
	dict['id3'] = resp1_json['id']
​
	req4JSON = urllib.request.Request('http://localhost:8001/id/4/')
	resp4 = urllib.request.urlopen(req4JSON).read().decode('utf-8')
	resp4_json = json.loads(resp4)
​
	dict['name4'] = resp4_json['name']
	dict['color4'] = resp4_json['color']
	dict['id4'] = resp1_json['id']
​
	req5JSON = urllib.request.Request('http://localhost:8001/id/5/')
	resp5 = urllib.request.urlopen(req5JSON).read().decode('utf-8')
	resp5_json = json.loads(resp5)
​
	dict['name5'] = resp5_json['name']
	dict['color5'] = resp5_json['color']
	dict['id5'] = resp1_json['id']
​
	req6JSON = urllib.request.Request('http://localhost:8001/id/6/')
	resp6 = urllib.request.urlopen(req6JSON).read().decode('utf-8')
	resp6_json = json.loads(resp6)
​
	dict['name6'] = resp6_json['name']
	dict['color6'] = resp6_json['color']
	dict['id6'] = resp1_json['id']
​
	return HttpResponse(json.dumps(dict), content_type="application/json") 
​
def detail(request, sock_id):
	#request from model the details for page
	req = urllib.request.Request('http://localhost:8001/id/' + sock_id + '/')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	return HttpResponse(json.dumps(resp_json), content_type="application/json")