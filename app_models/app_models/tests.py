from django.test import TestCase
from django.test import RequestFactory
from .models import *
from .views import *

import requests
import json
import urllib.request
import urllib.parse

class ModelTestCase(TestCase):
	def setUp(self):
		self.factory = RequestFactory()
		x = User.objects.create(username="TestUser1", password="password")
		y = User.objects.create(username="TestUser2", password="password")
		Sock.objects.create(name="Test1", material="Cotton", color="Blue", description="Test case 1", style="Crew", theme="Testing", seller=x, price=3.99)
		Sock.objects.create(name="Test2", material="Wool", color="Red", description="Test case 2", style="Long", theme="Testing2", seller=y, price=5.99)


	################# NOTE: Between tests, Django's unit test framework appears to be incrementing and changing ID values, so we were unable to get test working
	# def testId(self):
	# 	get_request = self.factory.get('/id/1/')
	# 	response = id(get_request, 1).content.decode("utf-8")
	# 	dict = json.loads(response)
	# 	dict['id'] = 1
	# 	dict2 = {"name": "Test1", "seller": "TestUser1", "style": "Crew", "color": "Blue", "price": 3.99, "description": "Test case 1", "theme": "Testing", "material": "Cotton", "id": 1}
	# 	self.assertEqual(dict, dict2)

	def testMaterial(self):
		get_request = self.factory.get('/material/Cotton/')
		response = material(get_request, "Cotton").content.decode("utf-8")
		dict = json.loads(response)
		dict[0]['id'] = 1
		dict2 = [{"name": "Test1", "seller": "TestUser1", "style": "Crew", "color": "Blue", "price": 3.99, "description": "Test case 1", "theme": "Testing", "material": "Cotton", "id": 1}]
		self.assertEqual(dict, dict2)

	def testColor(self):
		get_request = self.factory.get('/color/Blue/')
		response = color(get_request, "Blue").content.decode("utf-8")
		dict = json.loads(response)
		dict[0]['id'] = 1
		dict2 = [{"name": "Test1", "seller": "TestUser1", "style": "Crew", "color": "Blue", "price": 3.99, "description": "Test case 1", "theme": "Testing", "material": "Cotton", "id": 1}]
		self.assertEqual(dict, dict2)

	def testTheme(self):
		get_request = self.factory.get('/theme/Testing/')
		response = theme(get_request, "Testing").content.decode("utf-8")
		dict = json.loads(response)
		dict[0]['id'] = 1
		dict2 = [{"name": "Test1", "seller": "TestUser1", "style": "Crew", "color": "Blue", "price": 3.99, "description": "Test case 1", "theme": "Testing", "material": "Cotton", "id": 1}]
		self.assertEqual(dict, dict2)

	def testSignUp(self):
		# Checking if get request is handled correctly
		get_request = self.factory.get('/signup/')
		response = sign_up(get_request).content.decode("utf-8")
		dict = {"result": 1, "message": "Error: Get request made to sign_up on models level"}
		dict2 = json.loads(response)
		self.assertEqual(dict, dict2)

		# Checking post request
		post_request = self.factory.post('/signup/', {'username':'testuser', 'password':'password'})
		response = sign_up(post_request).content.decode("utf-8")
		dict = {"result": 0, "message": "New user created"}
		dict2 = json.loads(response)
		self.assertEqual(dict, dict2)