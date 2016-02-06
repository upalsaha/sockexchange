from django.db import models

class Sock(models.Model):
	name = models.CharField(max_length=30)
	material = models.CharField(max_length=30)
	color = models.CharField(max_length=30)
	description = models.TextField(max_length=255)
	style = models.CharField(max_length=30)
	theme = models.CharField(max_length=30)
	seller = models.EmailField()
	price = models.DeceimalField()

class Review(models.Model):
	username = models.CharField(max_length=30)
	rating = models.IntegerField()
	review_text = models.TextField(max_length=255)
	review_title = models.CharField(max_length=30)
	date_published = models.DateField(auto_now_add=True)
	sock_reviewed = models.ForeignKey(Sock)

class Order(models.Model):
	customer_name = models.CharField(max_length=30)
	customer_email = models.EmailField()
	date_purchased = models.DateTimeField(auto_now_add=True)
	socks = models.ManyToManyField(Sock)