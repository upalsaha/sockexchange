from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse
from kafka import KafkaProducer
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
		return render('/home/')
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

def login(request):
	response = "invalid"
	# if request.method == 'GET':
	# 	return render('/login/')
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		url = 'http://' + settings.MODELS_API + ':8000/login' + '?' + 'username=' + username + '&' + 'password=' + password

		req = urllib.request.Request(url)
		response = urllib.request.urlopen(req).read().decode('utf-8')

	return HttpResponse(response, content_type="application/json")

def logout(request):
	if request.method == 'POST':
		auth = request.POST.get('auth')
		url = 'http://' + settings.MODELS_API + ':8000/logout' + '?' + 'auth=' + auth
		req = urllib.request.Request(url)
		response = urllib.request.urlopen(req).read().decode('utf-8')
	return HttpResponse(response)

def create(request):
	response = "invalid"
	if request.method == 'GET':
		return render('/home/')
	if request.method == 'POST':
		auth = request.POST.get('auth')
		if not auth:
			return HttpResponse('BAD')
		else:
			url = 'http://' + settings.MODELS_API + ':8000/verify' + '?auth=' + auth
			req = urllib.request.Request(url)
			response = urllib.request.urlopen(req).read().decode('utf-8')
			if response == 'OK':
				url2 = 'http://' + settings.MODELS_API + ':8000/create/'
				name = request.POST.get('name')
				material = request.POST.get('material')
				color = request.POST.get('color')
				description = request.POST.get('description')
				style = request.POST.get('style')
				theme = request.POST.get('theme')
				price = request.POST.get('price')

				post_data = {'name': name, 'material': material, 'color': color, 'description': description, 'style': style, 'theme': theme, 'price': price, 'auth': auth}
				enc_data = urllib.parse.urlencode(post_data)
				bin_data = enc_data.encode('ascii')
				req2 = urllib.request.Request(url2)
				result = urllib.request.urlopen(req2, bin_data).read().decode('utf-8')

				# TODO: Add validation for listing
				producer = KafkaProducer(bootstrap_servers='kafka:9092')
				post_data['id'] = result
				producer.send('new-listings-topic', json.dumps(post_data).encode('utf-8'))

				return HttpResponse(result)